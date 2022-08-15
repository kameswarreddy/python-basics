# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:46:15 2022

@author: Bharath kuamr reddy
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
df = pd.read_csv("C:\\Users\Bharath kuamr reddy\\timrseries_data02.csv",parse_dates=True,index_col='Month')
df1 = df.head(100)
df1.info()
df1.plot()
df2 = pd.DataFrame(df1['Thousands of Passengers'], df1['Index'])
from statsmodels.tsa.arima_model import ARIMA
model = ARIMA(df1['Thousands of Passengers'], order=(0, 1, 1)) 
results_ARIMA = model.fit()