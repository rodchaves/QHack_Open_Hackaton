# QHack Open Hackaton

Portfolio optimization is the optomization problem where you have a number of assets and seek to answer the question: which asset should I acquire to maximize my profit in the future? By doing it so, it minimizes risk and maximizes returns of a collection of assets, also a called a portfolio. The process is not as easy as it seems. In 1952, Markowitz showed that risks and returns are usually linked, so high rewards are usually associated to high risks. 

Hybrid algorithms uses the fact that we can translate a optimization problem to one that is solvable by a quantum computer. Then, the quantum computer is used to solve one instance of the problem, a classical computer optimize the parameters used, and it runs another instance of the problem again in the quantum computer. Their names comes exactly from the fact that it is a mix of classical and quantum computers.

In this project I use both QAOA and VQE in Qiksit and Pennylane to optimize the problem for four assests: VALE, PBR, PFE, and HPE. I gave a brief explanation of how the problem is solved in a quantum computer and how the hydrid algorithms work. We also check that the results obtained in both algorithms are equal. We will see that the optimal result is acquiring PFE and HPE when we have a budget of 2, i.e. when we can only buy two assets.

The webscrapping from Yahoo! Finance was possible by the use of [this repository](https://github.com/c0redumb/yahoo_quote_download).
