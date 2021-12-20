
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
    trained_model_path = os.path.join(os.environ['MODEL_RAW_PATH'],'model_LSTM.h5')
    preprocess_data_path = os.path.join(os.environ['PREPROCESS_DATA_PATH'],"preprocessed_binance")
    model = keras.experimental.load_from_saved_model(trained_model_path)
    predictions=model.predict(preprocess_data_path )
    predictions_json=json.dumps(predictions.tolist())

    app= Flask(__name__)
    @app.route('/',methods=['GET'])
    def api_description():
        return jsonify({'El modelo predice ':predictions_json})
    app.run(debug=True)

#%tb
if __name__=='__main__':
    main()
