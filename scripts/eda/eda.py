# -*- coding: utf-8 -*-
"""eda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rAYRqb-djuWOe6vqVt6rmZMUbCTU2Spp
"""

from math import sqrt
from numpy import array
from numpy import mean
from numpy import std
import pandas as pd
from pandas import DataFrame
from pandas import concat
from pandas import read_csv
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import LSTM

from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from matplotlib import pyplot
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from sklearn import metrics


from keras.callbacks import ModelCheckpoint
from keras.layers import CuDNNLSTM
from tensorflow.keras import activations

import tensorflow as tf
import plotly.express as px
import seaborn as sns

series=pd.read_csv('supplemental_train.csv')
info=pd.read_csv('asset_details.csv')

series.head(10)

series_bitcoin = series[series['Asset_ID']==1]
series_bitcoin = series_bitcoin.set_index("timestamp")
df_train = pd.merge(series, info, how="left", on=["Asset_ID"])

info_s=info.sort_values("Weight")
fig_index=px.bar(info_s,x="Asset_Name" , y="Weight", color="Weight", title="distribucion de pesos de las crptomonedas ")
fig_index.show()
df = df_train.dropna()
plt.subplots(figsize=(20,10))
sns.countplot(x='Asset_Name', data = df)



#Comparamos el comportamiento general de tres criptomonedas y vemos que en general su compostamiento es bastante similar. 
import plotly.graph_objects as go

btc_mini = series_bitcoin.iloc[-200:] 
fig = go.Figure(data=[go.Candlestick(x=btc_mini.index, open=series[series['Asset_ID']==1].iloc[-200:]['Open'], high=series[series['Asset_ID']==1].iloc[-200:]['High'], low=series[series['Asset_ID']==1].iloc[-200:]['Low'], close=series[series['Asset_ID']==1].iloc[-200:]['Close'])])
fig.update_layout(
    title={'text': 'Bitcoin','y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
fig.show()
 
fig = go.Figure(data=[go.Candlestick(x=btc_mini.index, open=series[series['Asset_ID']==6].iloc[-200:]['Open'], high=series[series['Asset_ID']==6].iloc[-200:]['High'], low=series[series['Asset_ID']==6].iloc[-200:]['Low'], close=series[series['Asset_ID']==6].iloc[-200:]['Close'])])
fig.update_layout(
    title={'text': 'Etereum','y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
fig.show()

fig = go.Figure(data=[go.Candlestick(x=btc_mini.index, open=series[series['Asset_ID']==4].iloc[-200:]['Open'], high=series[series['Asset_ID']==4].iloc[-200:]['High'], low=series[series['Asset_ID']==4].iloc[-200:]['Low'], close=series[series['Asset_ID']==4].iloc[-200:]['Close'])])
fig.update_layout(
    title={'text': 'Dogecoin','y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
fig.show()

fig, axes = plt.subplots(7, 2, figsize=(20, 50))
df['fulldate'] = pd.to_datetime(df['timestamp'], unit='s')
df['date'] = df['fulldate'].apply(lambda d: d.date())
df['time'] = df['fulldate'].apply(lambda d: d.time())
for i,asset in enumerate(info['Asset_Name']):
    df_crypt = df[df['Asset_Name'] == asset]
    sns.lineplot(x="date", y="VWAP", data=df_crypt, ax=axes[int(i/2),i%2])
    axes[int(i/2),i%2].set_title(asset)

# se grafican los cambios normalizados para ver de forma vizual la correlacion entre bitcoin y ethereum
import scipy.stats as stats

lret_btc = log_return(btc_mini_2021.Close)[1:]
lret_eth = log_return(eth_mini_2021.Close)[1:]
lret_btc.rename('lret_btc', inplace=True)
lret_eth.rename('lret_eth', inplace=True)

plt.figure(figsize=(8,4))
plt.plot(lret_btc);
plt.plot(lret_eth);
plt.show()

# Obtenemos la correlacion entre todas las criptomonedas.

logs=pd.DataFrame([])
for asset_id, asset_name in zip(info.Asset_ID, info.Asset_Name):
    asset=series[series["Asset_ID"]==asset_id].set_index("timestamp")
    asset=asset.loc[totimestamp("01/01/2021"):totimestamp("21/09/2021")]
    asset=asset.reindex(range(asset.index[0],asset.index[-1]+60,60), method="pad")
    lret=log_return(asset.Close.fillna(0))[1:]
    logs=all2021.join(lret,rsuffix=asset_name,how="outer")
    
plt.imshow(logs.corr());
plt.yticks(info.Asset_ID, info.Asset_Name.values)
plt.xticks(info.Asset_ID, info.Asset_Name.values,rotation="vertical");
plt.colorbar()