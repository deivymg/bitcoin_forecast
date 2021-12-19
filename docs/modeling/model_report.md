# Final Model Report
_Report describing the final model to be delivered - typically comprised of one or more of the models built during the life of the project_

MODELO CuDNNLSTM - LSTM 

El modelo presentado para este proyecto se define como un modelo de Redes Neuronales Recurentes Bidireccional con Memoria de Largo-corto plazo, esto es asi debido a que se debe de realizar la predicción de un periodo de tiempo de la criptomoneda.



## Analytic Approach
* El target del proyecto es dar una predicción del precio futuro de la criptodivisa 
* Las entradas para el modelo son las proporcionadas por la API de Binance:
    * Open: precio de apertura de la criptodivisa en el periodo de  un minuto. 
    * High: Precio más alto de la criptodivisa en el periodo de  un minuto. 
    * Low: Precio más bajo de la criptodivisa en el periodo de  un minuto. 
    * Close: precio de cierre de la criptodivisa en el periodo de  un minuto. 
    
* Se utilizó un modelo de Redes Neuronales Recurrentes, debido a que este problema es un problema de series de tiempo que necesitan tener en cuenta el valor de la divisa en instantes de tiempo anteriores para predecir el valor en el futuro proximo - inmediato.

## Solution Description

*Simple solution architecture (Data sources, solution components, data flow)
* la salida del modelo es la predicción del modelo a un valor futuro de la divisa (target).

## Data
* los datos son extraidos a traves de la web API de Binance, esta nos ofrece los datos de la criptomoneda en cuestion (BITCOIN). primero se genera un request a la API para que nos enterge la informacion del historico de BITCOIN en un periodo de 15 min.

* Los datos son preprocesados y luego se integra se normalizan con un standar scaller

* Los datos con los que se haran las predicciones son todos los klines agrupados porminuto durante el ultimo dia en curso, esto debido a que se requiere calcular el vwap que es una valor calculado a diario.

* Rango de trabajo ultimas 24 horas de datos

* Medicion  Mse

## Features

* la mejor clasificación que le podemos dar a las variablems de foma Ordinal es la siguiente:

    Close
    Open
    Date
    High
    Low
    vwap


## Algorithm

![image](https://user-images.githubusercontent.com/21108295/146693871-86f8a757-de2d-4fd5-bfd6-3ab5db6950fc.png)

* El modelo se puede encontrar entrenado [aqui](https://github.com/deivymg/bitcoin_forecast/blob/master/scripts/modeling/model_CuDNNLSTM.h5)
	* 50 neuronsa CuDNNLSTM 
	* Activación Relu
	* Epocas de entrenamiento en calentamiento: 3
	* Epocas de entrenamiento: 100
		* validation_steps: 50
		* Medición de error Mean Square Error
* learning rate: 1x10^-5
* Learner hyper-parameters


## Results

las evalucaciones sobre el modelo se dieron con las siguientes caracteristicas.

* valuation metric results:-
MSE is : 4.3382098817287355e-06
MAE is : 0.0014370301978646467
RMSE is : 0.0020828369791533697
R2 is : -0.3962299464998571

![image](https://user-images.githubusercontent.com/21108295/146694010-5d9ecf0e-e68a-42ee-8c24-8a948bd89d79.png)
