"""Acutocorrealtion function"""

import pandas as pd
from statsmodels.graphics import tsaplots
import matplotlib.pyplot as plt

# Read in CSV data to Dataframe
df = pd.read_csv('TSLA.csv')
# Drop all columns but 'Date' and 'Adj Close', reindex using 'Date'
df = df[['Date', 'Adj Close']].set_index(['Date'])
# Check if any null or NaN values in data
df.isnull().sum()

data  = df['Adj Close']
data.plot(figsize=(8, 5))
#ploting ACF
fig = tsaplots.plot_acf(data, lags=30)
plt.show()