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
* la salida del modelo es la predicción del modelo a un valor futuro de la divisa.

## Data
* los datos son extraidos a traves de la web API de Binance, esta nos ofrece los datos de la criptomoneda en cuestion (BITCOIN). primero se genera un request a la API para que nos enterge la informacion del historico de BITCOIN en un periodo de 15 min.

* Data Schema

* Sampling

* Selection (dates, segments)

* Stats (counts)

## Features

* List of raw and derived features 
* la mejor clasificación que le podemos dar a las variablems de foma Ordinal es la siguiente:

    Close
    Open
    Date
    High
    Low


## Algorithm
* Modelo LSTM de 50 capas intermedias, Una capa densa y un Optimizador Adam

	* Description or images of data flow graph
  		* if AzureML, link to: (Imagen del modelo)
    		* Training experiment
    		* Scoring workflow
* learning rate: 1x10^-3

* Learner hyper-parameters

## Results
* valuation metric results:-
MSE is : 4.3382098817287355e-06
MAE is : 0.0014370301978646467
RMSE is : 0.0020828369791533697
R2 is : -0.3962299464998571

* Performance graphs for parameters sweeps if applicable
