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
| Processed Crypto Competition  | [kaggle dataset](https://www.kaggle.com/cstein06/tutorial-to-the-g-research-crypto-competition/data) | [Python_limpiezadatoscsv.py](link/to/python/script/file/in/Code) | [Processed Crypto Competition Report](link/to/report1)|
| Processed Binance API | [JSON](link/to/dataset2/report) |[jsonprocessscript.py](link/to/R/script/file/in/Code) | [Processed Binance API Report](link/to/report2)|
* Processed Crypto Competition summary. se crea un scrip de limpieza de datos faltantes y aplicar una normalización de los datos
* Processed Binance API summary. Se crea un script para evaluar los datos y recibidos por el api y determinar si estan correctamente y aplicar normalización.

> 
