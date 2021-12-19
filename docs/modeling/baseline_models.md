# Baseline Model Report

Se elaboraron dos modelos para evaluar el mejor desempeño uno con redes LSTM y otro Con redes LSTM RNN o recurrentes.


MODELO LSTM Long Short Term Memory Multivariable

Las redes  Long Short Term Memory (LSTM), son muy usadas en el ambito de predeccion en lineas de tiempo, por lo tanto en la elaboración de nuestro modelo se creara una red neuronal basada en esta clase de neuronas.

Se creara un modelo con una capa LSTM con 50 neuronas intermedias como modelo inicial, a partir de este modelo se van a realizar cambios para ajustarlo a la necesidad del proyecto.

## Analytic Approach
* El modelo predicira el atributo Target de los datos, recordemos que este es la representacion de los rendimientos en formato log residual de los proximos 15 minutos, por lo que con la prediccion de este valor nuestro modelo sera capaz de predecir el comportamiento a nivel de rendimientos de la criptomoneda en los proximos 15 minutos. 

* Las entradas para el modelo son las proporcionadas por la API de Binance:
    * Timestamp: estampa de minuto que representa este kline. 
    * Open: precio de apertura de la criptodivisa en el periodo de  un minuto. 
    * High: Precio más alto de la criptodivisa en el periodo de  un minuto. 
    * Low: Precio más bajo de la criptodivisa en el periodo de  un minuto. 
    * Close: precio de cierre de la criptodivisa en el periodo de  un minuto. 
    * VWAP: Valor de precio medio ponderado por volumen. 
* Salida:
    * Target: Prediccion del los rendimientos en log residual de los proximos 15 minutos de la criptomoneda. 
    

## Model Description
# Modelo LSTM de 1 capa intermedias, Una capa densa y un Optimizador Adam

* Se utilizó un modelo de LSTM, debido a que este problema es un problema de series de tiempo que necesitan tener en cuenta el valor de la divisa en instantes de tiempo anteriores para predecir el valor en el futuro proximo - inmediato.


La siguiente imagen muestra la grafica de como se ve el modelo LSTM \
![image](https://user-images.githubusercontent.com/21108295/146693189-146b66a0-df57-47d5-a78f-87a2dbbaa0b7.png)


	* El modelo se puede encontrar entrenado [aqui](https://github.com/deivymg/bitcoin_forecast/blob/master/scripts/modeling/model_LSTM.h5)
  		* 50 neuronsa LSTM 
  		* Activación Relu
  		* Epocas de entrenamiento: 100
    		* validation_steps: 50
    		* Medición de error Mean Square Error
	* learning rate: 1x10^-3
	* Learner hyper-parameters
Perdida del modelo 

![image](https://user-images.githubusercontent.com/21108295/146693343-00e3540b-0be5-4420-9dc4-f071373ac5c2.png)
\

Como se evidencia en el modelo, este tiene un buen desempeño en cuanto a peridad en validación

# Modelo CuDNNLSTM de 3 capas con dropout de 20% y finetunning


Tamibien se diseño un modelo basado en Redes Recurrentes en los que la salida tambien se puede usar como entrada para el mismo. Estas redes RNN a diferencia de las LSTM tradicionales tiene una memoria mas corta, por lo que permitira evaluar si este tipo de precciones es mas acertada que las del otro modelo evaluado.


	* El modelo se puede encontrar entrenado [aqui](https://github.com/deivymg/bitcoin_forecast/blob/master/scripts/modeling/model_CuDNNLSTM.h5)
  		* 50 neuronsa CuDNNLSTM 
  		* Activación Relu
  		* Epocas de entrenamiento en calentamiento: 3
  		* Epocas de entrenamiento: 100
    		* validation_steps: 50
    		* Medición de error Mean Square Error
	* learning rate: 1x10^-5
	* Learner hyper-parameters
Perdida del modelo 

![image](https://user-images.githubusercontent.com/21108295/146693461-38862087-21ce-4c87-b26e-91b3a56c688f.png)
\


## Results (Model Performance) LSTM
* Evaluation metric results:-
Evaluation metric results:- \
MSE is : 0.00010182643872599576 \
MAE is : 0.006106787879975921 \
RMSE is : 0.010090908716562437 \
R2 is : -31.77230170293499 \

## Results (Model Performance) CuDNNLSTM
Evaluation metric results:- \
MSE is : 4.3382098817287355e-06 \
MAE is : 0.0014370301978646467\ 
RMSE is : 0.0020828369791533697\
R2 is : -0.3962299464998571\



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
