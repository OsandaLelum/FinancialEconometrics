# -*- coding: utf-8 -*-
"""
The purpose is to load data from csv and then to perform basic statistical
analysis, testing for normality, plotting, return convertion and to calculate 
percentiles non-parametrically.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
from scipy import stats

# Read in CSV data to Dataframe
df = pd.read_csv('AAPL.csv')
# Drop all columns but 'Date' and 'Adj Close', reindex using 'Date'
data = df[['Date', 'Adj Close']].set_index(['Date'])
# Check if any null or NaN values in data
df.isnull().sum()

price  = df['Adj Close']
mean = np.mean(price)
stdv = np.std(price)
kurto = kurtosis(price, bias=False)
skewness = skew(price, bias=False)
jarque_bera_test = stats.jarque_bera(price)
price.plot(figsize=(8, 5))
plt.show()

def qunatile(alpha, data):
    ret=np.zeros(len(data))
    for t in range(1, len(data)):
        ret[t] =100*(np.log(data[t]) - np.log(data[t-1]))
    T=len(ret)
    order_data = np.sort(ret)
    if alpha < 1/T:
        q_alpha = min(order_data)
    elif alpha > (T-0.5)/T:
        q_alpha = max(order_data)
    else:
        q_alpha = order_data[int(np.ceil(alpha*T))]
    return q_alpha
