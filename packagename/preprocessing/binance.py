import numpy as np
import pandas as pd
from pandas import DataFrame
from datetime import datetime
import time
import sklearn
from sklearn.preprocessing import StandardScaler



'''
LIMPIEZA DE LOS DATOS OBTENIDOS DEL DATASET EN CSV
'''


def preprocessing(series_bitcoin: DataFrame) :

  df = series_bitcoin
  Y = series_bitcoin['Target']
  X = series_bitcoin.drop('Target', axis=1)
  
    # Estandarizamos los datos
  scaler = StandardScaler()

  X_btc_scaled = scaler.fit_transform(df)

  x_final = prepararDataset(X_btc_scaled,Y)
  x_total,y_total  = split_sequences(x_final, 15)
  return (x_total)

def prepararDataset(x,y):

  # convertimos a un arreglo
  x = np.array(x)
  y = np.array(y)

  x0 = x[:,0].reshape(x.shape[0], 1)  # corresponde a Count
  x1 = x[:,1].reshape(x.shape[0], 1)  # corresponde a Open
  x2 = x[:,2].reshape(x.shape[0], 1)  # correpsonde a High
  x3 = x[:,3].reshape(x.shape[0], 1)  # corresponde a Low
  x4 = x[:,4].reshape(x.shape[0], 1)  # corrresponde a Close
  x5 = x[:,5].reshape(x.shape[0], 1)  # corresponde a Volume
  x6 = x[:,6].reshape(x.shape[0], 1)  # corresponde a VWAP

  y = y.reshape(x.shape[0], 1)

  dataset = np.hstack((x0,x1,x2,x3,x4,x5,x6,y))

  return dataset

# Dividir la secuencia multivariable en muestras
def split_sequences(sequences, n_steps):
  X, y = list(), list()
  for i in range(len(sequences)):
    # encontrar el final de la muestra
    end_ix = i + n_steps
    # control para cuando hayamos llegado al final de la secuenciat
    if end_ix > len(sequences):
      break
  # Encontrar secuencia y adicionarla
    seq_x = sequences[i:end_ix, :-1]
    seq_y = sequences[end_ix-1, -1]
    X.append(seq_x)
    y.append(seq_y)
  return np.array(X), np.array(y)
