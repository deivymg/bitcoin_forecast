import os
import pandas as pd
import numpy as np
import tensorflow as tf
import keras

def main():

	data_path = os.path.join(os.environ['PREPROCESS_DATA_PATH'],"preprocessed_data.npz")
	data_train_test = np.load(data_path)
	x_train = data_train_test['x_train']
	y_train = data_train_test['y_train']
	x_test = data_train_test['x_test']
	y_test = data_train_test['y_test']

	model_path = os.path.join( os.environ['MODEL_PATH'],"model_LSTM.h5")
	model =tf.keras.models.load_model(model_path)

	loss, acc = model.evaluate(x_test, y_test)
	print('Restored model, accuracy: {:5.2f}%'.format(100 * acc))





if __name__ == "__main__":
	main()
 




