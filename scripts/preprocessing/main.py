import os 
import pandas as pd
import numpy as np
from packagename.preprocessing.preprocessing import prepararDataset,split_sequences,limpieza,preprocessing

def main():
	data_path = os.path.join(os.environ['BTC_DATAFRAME_PATH'],'supplemental_train.csv')
	print(data_path)
	series=pd.read_csv(data_path)
	series_bitcoin=limpieza(series)
	x_train,y_train,x_test,y_test = preprocessing(series_bitcoin)
	#data = preprocessing(series_bitcoin)
	#names=["x_train","y_train","x_test","y_test"]
	
	save_path = os.path.join(os.environ['PREPROCESS_DATA_PATH'],"preprocessed_data")
	print(save_path)
	np.savez(save_path,x_train = x_train,y_train = y_train,x_test = x_test,y_test = y_test)
		
	#x_train.tofile('x_train')
	#y_train.tofile('y_train')
	#x_test.tofile('x_test')
	#y_test.tofile('y_test')
  	
if __name__=="__main__":
  main()
