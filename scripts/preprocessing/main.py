
import os 
import pandas as pd
import numpy as np
from packagename.preprocessing.preprocessing import prepararDataset,split_sequences,limpieza,preprocessing


#funcion de flujo principal
def main():
	data_path = os.path.join(os.environ['BTC_DATAFRAME_PATH'],'supplemental_train.csv')
	print(data_path)
	series=pd.read_csv(data_path)
	series_bitcoin=limpieza(series)
	x_train,y_train,x_test,y_test = preprocessing(series_bitcoin)
		
	save_path = os.path.join(os.environ['PREPROCESS_DATA_PATH'],"preprocessed_data")
	print(save_path)
	#se almacenan los datos serializados (juntos)
	np.savez(save_path,x_train = x_train,y_train = y_train,x_test = x_test,y_test = y_test)
		
  	
if __name__=="__main__":
  main()
