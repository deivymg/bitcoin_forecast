from flask import Flask, request, jsonify
from pydantic import BaseModel, Field
import numpy as np
import bitcoin_forecast.scripts.data_acquisition.main as data_acquisition
import bitcoin_forecast.scripts.preprocessing.binance as preprocessing
import os
import json
from tensorflow import keras



app= Flask(__name__)

class APIInput(BaseModel):
    #numpyArray: np.ndarray = Field(default_factory=lambda: np.zeros(10))
    numpyArray: str 
    class Config:
        arbitrary_types_allowed = True

@app.route('/',methods=['GET'])
def api_description():
    return jsonify({'description':'simple api to get predictions'})
'''
@app.route('/',methods=['POST'])
def predict_evaluation():
    data=request.json
    try:
        input_data=APIInput(**data)
    except: 
        return jsonify({'error':'Invalid input data'}), 400
    print(input_data)
    return jsonify({'prediction':'Hello!!'})
'''

#Carga los datos mediante a api de binance de los ultimos 15 minutos.
#Preprocesa los datos y los carga en un path conocido.
#Carga el modelo preentrenado desde un path conocido 
#Realiza las predicciones del modelo con los datos preprocesados y los muestra en la api. 

def main():
    data_acquisition.main()
    preprocessing.main()
    trained_model_path_1 = os.path.join(os.environ['MODEL_RAW_PATH_1'],'model_LSTM.h5')
    trained_model_path_2 = os.path.join(os.environ['MODEL_RAW_PATH_2'],'model_CuDNNLSTM.h5')
    preprocess_data_path = os.path.join(os.environ['PREPROCESS_DATA_PATH'],"preprocessed_binance")
    model1 = keras.experimental.load_from_saved_model(trained_model_path_1)
    model2 = keras.experimental.load_from_saved_model(trained_model_path_2)
    predictions_1=model1.predict(preprocess_data_path )
    predictions1_json=json.dumps(predictions_1.tolist())
    predictions_2=model2.predict(preprocess_data_path )
    predictions2_json=json.dumps(predictions_2.tolist())

    app= Flask(__name__)
    @app.route('/prediction1',methods=['GET'])
    def api_description():
        return jsonify({'El modelo CuDNNLSTM predice ':predictions1_json})

    @app.route('/prediction2',methods=['GET'])
    def api_description():
        return jsonify({'El modelo LSTM predice ':predictions2_json})
    app.run(debug=True)

#%tb
if __name__=='__main__':
    main()
