# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:21:42 2021

@author: Rodrigo Chaves
"""

import pandas as pd
import numpy as np
import yfscraping as yf

#Function to pull the history of a stock from Yahoo! Finance and save it in a data frame
def Stock_Data(stock, startdate, enddate):
    
    #Pull the data from Yahoo! Finance and create a dataframe called data
    #The function load_yahoo_quote return a list of strings, then I need to split the strings into lists for the dataframe
    yf_data = yf.load_yahoo_quote(stock, startdate, enddate)
    data_process=[]
    days = []
    for i in range(len(yf_data)):
        data_process.append(yf_data[i].split(','))
    
    #Each entry of the list will be a string with date, set as YYYYMMDD, open value, highest value in the day, minimum
        #value, volume, adj close, and close value
    #Again, we need to split the string to get each column of the data frame
    data_process.pop(0)
    data = pd.DataFrame(data_process,columns=yf_data[0].split(','))
    
    #We dont care about specific date, only the number of days
    for day in range(len(data.Date)):
        days.append(day+1)

    data['Days']=days
    data = data.drop('Date',axis=1)
    data = data.apply(pd.to_numeric)
    return data

#Function that gets the desired stocks and outputs their close value in a np.array
def Stocks_Array(num_assets, stocks, startdate='20160101', enddate='20211001'):
    days = []
    stock = []
    #Loop to append each close value array to stock
    for stk in stocks:
        data = Stock_Data(stk, startdate, enddate)
        stock.append(data['Close'])
    
    #We only care about the number of days and not the date itself
    days.append(data['Days'])
    return days, stock

#Function to get the mu value which is the mean of each stock multiplied by a weight
def Get_Mu_Cov(stocks, num_assets, weight):
    mu = np.zeros(num_assets)
    for asset in range(num_assets):
        mu[asset] = weight[asset]*stocks[asset].mean()
    cov = np.cov(stocks)
    return mu,cov