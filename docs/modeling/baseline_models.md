# Baseline Model Report

MODELO LSTM Long Short Term Memory Multivariable

Se va a utilizar un modelo de LSTM con 50 neuronas intermedias como modelo inicial, a partir de este modelo se van a realizar cambios para ajustarlo a la necesidad del proyecto.


## Analytic Approach
* El target del proyecto es dar una predicción del precio futuro de la criptodivisa 
* Las entradas para el modelo son las proporcionadas por la API de Binance:
    * Open: precio de apertura de la criptodivisa en el periodo de  un minuto. 
    * High: Precio más alto de la criptodivisa en el periodo de  un minuto. 
    * Low: Precio más bajo de la criptodivisa en el periodo de  un minuto. 
    * Close: precio de cierre de la criptodivisa en el periodo de  un minuto. 
    
* Se utilizó un modelo de LSTM, debido a que este problema es un problema de series de tiempo que necesitan tener en cuenta el valor de la divisa en instantes de tiempo anteriores para predecir el valor en el futuro proximo - inmediato.

## Model Description

* Modelo LSTM de 50 capas intermedias, Una capa densa y un Optimizador Adam

	* Description or images of data flow graph
  		* if AzureML, link to: (Imagen del modelo)
    		* Training experiment
    		* Scoring workflow
	* learning rate: 1x10^-3
	* Learner hyper-parameters


## Results (Model Performance)
* Evaluation metric results:-
MSE is : 0.00010182643872599576
MAE is : 0.006106787879975921
RMSE is : 0.010090908716562437
R2 is : -31.77230170293499

* Performance graphs for parameters sweeps if applicable

## Model Understanding

* la mejor clasificación que le podemos dar a las variablems de foma Ordinal es la siguiente:

    Close
    Open
    Date
    High
    Low



## Conclusion and Discussions for Next Steps

* Conclusion on Feasibility Assessment of the Machine Learning Task

* Discussion on Overfitting (If Applicable)

* What other Features Can Be Generated from the Current Data

* What other Relevant Data Sources Are Available to Help the Modeling
