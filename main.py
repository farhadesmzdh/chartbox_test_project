import yfinance as yf
import pandas as pd
import numpy as np

''''' getting AAPL recent year price in daily timeframe '''''
data = yf.download("aapl", period='1y', interval='1d')


''''' we have to add a new column to dataframe to show whether candle is ascending(ASC) or descending(DESC)
we can do it in 2 ways: 
    I) vectorized way
    II) none-vectorized way by using pandas apply 
    vectorized way is much faster than none-vectorized way '''''


data.loc[data['Close'] > data['Open'], 'Candle'] = 'ASC'
data.loc[data['Close'] < data['Open'], 'Candle'] = 'DESC'

''''' another vectorized ways to add column:
I) using pandas apply:
def check_candle(open, close):
    return 'ASC' if close > open else 'DESC'
    
data['Candle'] = data.apply(lambda x: check_candle(x['Open'], x['Close']), axis=1)

II) using numpy select:
data['Candle'] = np.select([(data['Close'] > data['Open']) , (data['Close'] <= data['Open'])], ['ASC', 'DESC'])

III) using numpy where:
data['Candle'] = np.where((data['Close'] > data['Open']), 'ASC', 'DESC')
'''''

print(data[['Open', 'High', 'Low', 'Close', 'Candle']])
