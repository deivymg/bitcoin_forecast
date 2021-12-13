'''
LIMPIEZA DE LOS DATOS OBTENIDOS DEL DATASET EN CSV
'''

def limpieza(df:DataFrame ) -> DataFrame:
  series_bitcoin = df[df['Asset_ID']==1]
  series_bitcoin = series_bitcoin.set_index("timestamp")
  series_bitcoin = series_bitcoin.dropna()
  #Rellenamos datos faltantes con el ultimo valor. 
  series_bitcoin = series_bitcoin.reindex(range(series_bitcoin.index[0],series_bitcoin.index[-1]+60,60),method='pad')
  return series_bitcoin

def preprosesing(series_bitcoin: DataFrame):

    # armamos el data set de entrada y el vector de salida y 

  Y = series_bitcoin['Target']
  X = series_bitcoin.drop('Target', axis=1)
  X = X.drop('Asset_ID', axis=1)

  totimestamp = lambda s: np.int32(time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple()))

  # Ecojemos nuestro dataset datos del 2021
  # BTC data va desde 2021-06-13T00:00:00 a 2021-09-20T23:44:00
  train_window = [totimestamp("01/06/2021"), totimestamp("30/07/2021")]
  test_window = [totimestamp("01/07/2021"), totimestamp("30/08/2021")]


  X_btc_train = X.loc[train_window[0]:train_window[1]]
  y_btc_train = Y.loc[train_window[0]:train_window[1]]

  X_btc_test = X.loc[test_window[0]:test_window[1]]
  y_btc_test = Y.loc[test_window[0]:test_window[1]]


  from sklearn.preprocessing import StandardScaler
  # Estandarizamos los datos
  scaler = StandardScaler()

  X_btc_train_scaled = scaler.fit_transform(X_btc_train)
  X_btc_test_scaled = scaler.transform(X_btc_test)

  n_steps = 15
  dataset_train = prepararDataset(X_btc_train_scaled,y_btc_train)
  x_train, y_train = split_sequences(dataset_train, n_steps)

  dataset_test = prepararDataset(X_btc_test_scaled,y_btc_test)
  x_test, y_test = split_sequences(dataset_test, n_steps)

  return x_train, y_train,x_test, y_test

def prepararDataset(x,y):

  # convertimos a un arreglo
  x =  array(x)
  y = array(y)

  x0 = x[:,0].reshape(x.shape[0], 1)  # corresponde a Count
  x1 = x[:,1].reshape(x.shape[0], 1)  # corresponde a Open 
  x2 = x[:,2].reshape(x.shape[0], 1)  # correpsonde a High
  x3 = x[:,3].reshape(x.shape[0], 1)  # corresponde a Low
  x4 = x[:,4].reshape(x.shape[0], 1)  # corrresponde a Close
  x5 = x[:,5].reshape(x.shape[0], 1)  # corresponde a Volume
  x6 = x[:,6].reshape(x.shape[0], 1)  # corresponde a VWAP

  y = y.reshape(x.shape[0], 1)

  dataset = hstack((x0,x1,x2,x3,x4,x5,x6,y))

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
  return array(X), array(y)
