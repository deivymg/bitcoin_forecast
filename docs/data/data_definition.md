# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

For each data, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided. 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided. 



## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Dataset Crypto Competition | Dataset CSV | [kaggle dataset](https://www.kaggle.com/cstein06/tutorial-to-the-g-research-crypto-competition/data) | [kaggle Report](https://www.kaggle.com/cstein06/tutorial-to-the-g-research-crypto-competition/notebook)|
| Binance API | Binance exchange REST API v3  |   [API Documentation](https://python-binance.readthedocs.io/en/latest/) | [Data strcuture](https://python-binance.readthedocs.io/en/latest/)|

* Dataset Crypto Competition . Datos de miles de las transacciones hechas por cada minuto en varias criptomonedas incluidas bitcoin.
* Binance API summary. Datos traídos a través de formato JSON de las transacciones para criptomoneda solicitada.

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Crypto Competition  | [kaggle dataset](https://www.kaggle.com/cstein06/tutorial-to-the-g-research-crypto-competition/data) | [Limpieza de datos](/scripts/preprocessing/main.py) | [Processed Crypto Report](/docs/data/data_preprocessing.md)|
| Processed Binance API | [API data acquisition and processing](/scripts/data_acquisition/main.py) |[Limpieza de datos](/scripts/preprocessing/main.py )| [Processed Crypto Report](/docs/data/data_preprocessing.md)| 


La limpieza de datos es la misma para los dos tipos de datos ya que se hizo una estandarizacion de los archivos y ambos tienen la misma estructura.

* Processed Crypto Competition summary. se crea un scrip de limpieza de datos faltantes y aplicar una normalización de los datos
* Processed Binance API summary. Se crea un script para evaluar los datos y recibidos por el api y determinar si estan correctamente y aplicar normalización.


## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Caracteristicas klines| [Processed Crypto Report](/docs/data/data_preprocessing.md) | [VWAP](https://github.com/deivymg/bitcoin_forecast/blob/master/docs/data/vwap.md) | [Feature Set1 Report](https://github.com/deivymg/bitcoin_forecast/blob/master/scripts/data_acquisition/data/preprocess/ultimos_15_minutos.csv)|


* Caracteristicas klines. Las caracteristicas extraidas para el analisis son: valor mas alto (High), valor mas bajo (Low), valor de apertura de la criptomoneda (Open), valor de cierre (Close) y el volumen de criptonedas transadas (Volumn) y Precio medio ponderado por volumen (VWAP)

