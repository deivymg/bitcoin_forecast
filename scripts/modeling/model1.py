import tensorflow as tf
from tensorflow.keras import activations

from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import LSTM

def main():

	model = Sequential()
	model.add(LSTM(50, activation="relu", input_shape=(15,7)))
	model.add(Dense(1))
	model.compile(loss="mse", optimizer=tf.optimizers.Adam(lr=1e-3))

	model_path = 'model_1_LSTM_Multivariate.h5'
	early_stopings = tf.keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=10, verbose=1, mode='min')
	checkpoint =  tf.keras.callbacks.ModelCheckpoint(model_path, monitor='val_loss', save_best_only=True, mode='min', verbose=True)


if __name__=="__main__":
  main()


