import os
import pandas as pd
import numpy as np
from packagename.preprocessing.binance import preprocessing


#funcion de flujo principal
def main():
	data_path = os.path.join(os.environ['BINANCE_RAW_PATH'],'ultimos_15_minutos.csv')
	print(data_path)
	series=pd.read_csv(data_path)
	df=series
	df.set_index('timestamp',inplace=True)
	x_real = preprocessing(df)
	save_path = os.path.join(os.environ['PREPROCESS_DATA_PATH'],"preprocessed_binance")
	print(save_path)
        #se almacenan los datos serializados (juntos)
	np.savez(save_path,x=x_real)


if __name__=="__main__":
  main()

