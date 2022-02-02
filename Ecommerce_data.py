# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:02:26 2022

@author: AARYA
"""

import pandas as pd 
import numpy as np
import sqlite3
import datetime as dt

conn = sqlite3.connect("Ecommerce_Xapix.db")

sql =   """ 
        SELECT * FROM financials 
        """

financials = pd.read_sql_query(sql,conn)

financials['month'] = pd.to_datetime(financials['postedDate']).dt.month
financials['Day'] = pd.to_datetime(financials['postedDate']).dt.day
financials['Year'] = pd.to_datetime(financials['postedDate']).dt.year

financials.isna().sum()

financials = financials.fillna(0)

financials.isnull().sum()

parameters = [('charge','principal'),('charge','shipping'),('charge','wrapping')]

def month_year():
    
    month = int(input(('select the month:')))
    year = int(input('select the year:'))

    i = 0
    
    sales = []
    
    while i < 3:
        
        df_select = financials.iloc[np.where((financials.month == month) & (financials.Year == year)
                                           & (financials.type == parameters[i][0]) & (financials.subType == parameters[i][1]))]
        
        charge_type = df_select.currencyAmount.sum()      
        sales.append(charge_type) 
        
        i+=1
        
    sum_charges = sum(sales)
        
    df_cost = financials.iloc[np.where((financials.month == month) & (financials.Year == year)
                                           & (financials.type == 'fee') | (financials.type == 'serviceFee'))]
    cost = df_cost.currencyAmount.sum()
    
    sales.append(sum(sales))
    sales.append(cost)
    sales.append(sum_charges+cost)
   
    return sales

def year_select(year):
    
    i = 0
    
    sales = []
    
    while i < 3:
        
        df_select = financials.iloc[np.where((financials.Year == year) & (financials.type == parameters[i][0]) & 
                                             (financials.subType == parameters[i][1]))]
        
        charge_type = df_select.currencyAmount.sum()      
        sales.append(charge_type) 
        
        i+=1
        
    sum_charges = sum(sales)
        
    df_fee = financials.iloc[np.where((financials.Year == year) & (financials.type == 'fee') | (financials.type == 'serviceFee'))]
    fee_sum = df_fee.currencyAmount.sum()
    
    sales.append(sum(sales))
    sales.append(fee_sum)
    sales.append(sum_charges+fee_sum)
    
    return sales

def get_df():
    df = pd.DataFrame(list(zip(['Product Sales','Shipping Revenue','Other Income','Total Sales','Cost','Total'],month_year(), month_year(), year_select(2021))),
           columns = ['Name','2021-01-01T00:00:00Z', '2021-02-01T00:00:00Z','2021'])
    
    return df

print(get_df())


### Sample Json files after converting to dataframe 




