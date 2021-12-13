from bitcoin_forecast.scripts.preprocessing.preprocessing import prepararDataset,split_sequences,limpieza,preprosesing

df main():
  series=pd.read_csv('train.csv')
  series_bitcoin=limpieza(series)
  x_train, y_train,x_test, y_test=preprosesing(series_bitcoin)
  x_train.tofile('x_train')
  y_train.tofile('y_train')
  x_test.tofile('x_test')
  y_test.tofile('y_test')
  
if __name__=="__main__":
  main()
