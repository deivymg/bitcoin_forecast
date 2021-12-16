import os 
import pandas as pd
import numpy as np
from packagename.preprocessing.preprocessing import prepararDataset,split_sequences,limpieza,preprocessing

def main():
	data_path = os.path.join(os.environ['BTC_DATAFRAME_PATH'],'supplemental_train.csv')
	print(data_path)
	series=pd.read_csv(data_path)
	print(series.head())
	series_bitcoin=limpieza(series)
  	#x_train,y_train,x_test,y_test = preprocessing(series_bitcoin)

	data=preprocessing(series_bitcoin)
	x_train=data[0]
	y_train=data[1]
	x_test=data[2]
	y_test=data[3]
	x_train.tofile('x_train')
	y_train.tofile('y_train')
	x_test.tofile('x_test')
	y_test.tofile('y_test')
  
if __name__=="__main__":
  main()
