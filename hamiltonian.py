# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:23:50 2021

@author: Rodrigo Chaves
"""

# Module dedicated to create the Ising Hamiltonian that will be used to construct
# the qaoa layers. Two Hamiltonians are required to build the layers: cost and mixer.

import pennylane as qml
from pennylane import numpy as np


# This function creates the Hamiltonian for portfolio optmization without adding
# the required constraints. It uses the risk factor q, the stock mean value mu,
# and the covariance matrix sigma. Every qubit corresponds to a stock and a 
# corresponding PauliZ matrix.



def Cost_Hamiltonian(num_assets, mu, sigma, q):
    const = []
    op = []
    sum_sigma = np.sum(sigma,axis=1)
    for i in range(num_assets):
        const.append(mu[i]/2-q*sum_sigma[i]/2)
        op.append(qml.PauliZ(i))
        for j in range(i,num_assets):
            if i != j:
                const.append(q*sigma[i,j]/4)
                op.append(qml.PauliZ(i)@qml.PauliZ(j))
    H = qml.Hamiltonian(const,op)
    return H

# The mixer Hamiltonian is just the application of a PauliX in every qubit.

def Mix_Hamiltonian(num_assets):
    const = [1]*num_assets
    op = []
    for i in range(num_assets):
        op.append(qml.PauliX(i))
    H = qml.Hamiltonian(const,op)
    return H

# This functions is the step that will add constraints to the cost Hamiltonian.
# Since it is a minimization problem, we will add a term to the Hamiltonian in a way
# that increases the energy value if the constraint is not satisfied. In other words
# we will add a term given by
#               +20(\sum z - budget)².
# Notice that if we have a solution that is lower ou higher than the budget, a 
# positive value will be added to the Hamiltonian.

def W_Cost_Hamiltonian(num_assets, mu, sigma, q, budget):
    const = []
    op = []
    A = 200
    for i in range(num_assets):
        const.append(A*(budget-num_assets/2))
        op.append(qml.PauliZ(i))
        for j in range(i,num_assets):
            if i != j:
                const.append(A/4)
                op.append(qml.PauliZ(i)@qml.PauliZ(j))
    H = qml.Hamiltonian(const,op) + Cost_Hamiltonian(num_assets, mu, sigma, q)      
    return H