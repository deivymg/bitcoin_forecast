import tensorflow as tf
from tensorflow.keras import activations

from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import LSTM
from keras.layers import CuDNNLSTM


def main():

	DROPOUT = 0.2
	WINDOW_SIZE = 50

	ft_model = Sequential()
	ft_model.add(tf.keras.layers.Bidirectional(CuDNNLSTM(WINDOW_SIZE, return_sequences=True),
	input_shape=(n_steps, n_features) ))
	ft_model.add(tf.keras.layers.Dropout(rate=DROPOUT))
	ft_model.add(tf.keras.layers.Bidirectional(CuDNNLSTM((WINDOW_SIZE * 2), return_sequences=True)))
	ft_model.add(tf.keras.layers.Dropout(rate=DROPOUT))
	ft_model.add(tf.keras.layers.Bidirectional( CuDNNLSTM(WINDOW_SIZE, return_sequences=False)))
	ft_model.add(Dense(units=1))
	ft_model.add(Activation('linear'))
	ft_model.compile(loss="mse", optimizer=tf.optimizers.Adam(learning_rate=1e-3))

	ft_model_path = 'model_1_LSTM_2.h5'
	ft_early_stopings = tf.keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=10, verbose=1, mode='min')


if __name__=="__main__":
  main()


