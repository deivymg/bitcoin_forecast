import os 
import numpy as np
import pandas as pd
import tensorflow as tf
import warnings
warnings.filterwarnings('ignore')

def main():

	data_path = os.path.join(os.environ['PREPROCESS_DATA_PATH'],'preprocessed_binance.npz')
	x_pred = np.load(data_path)
	model_path = os.path.join(os.environ['MODEL_PATH'],'model_LSTM.h5')
	model = tf.keras.models.load_model(model_path)
	y_pred = model.predict(x_pred['x'])
	print(f"prediccion del modelo: {y_pred[0]}")



if __name__ == "__main__":
	main()
