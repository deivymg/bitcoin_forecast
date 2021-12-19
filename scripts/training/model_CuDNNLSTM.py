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
	
	early_stopings = tf.keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=30, verbose=1, mode='min')
	checkpoint =  tf.keras.callbacks.ModelCheckpoint(model_path, monitor='val_loss', save_best_only=True, mode='min', verbose=True)
	callbacks=[early_stopings,checkpoint] 

	history = model.fit(x_train, y_train,
		 validation_data=(x_test, y_test), batch_size=64, epochs=100,steps_per_epoch=100,
		validation_steps=50,verbose=1,callbacks=callbacks)

	print(np.min(history.history['loss']))
	print(np.min(history.history['val_loss']))

	

if __name__ == "__main__":
	main()
 




