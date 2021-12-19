# Deployment

* Para desarrollar el modelo se usara un entorno de cofiguracion con pyenv y configurado con las indicaciones que encontrar en el archivo [Makefile](https://github.com/deivymg/bitcoin_forecast/blob/master/Makefile)

* La elaboración de los modelos de prediccion se usara python 3.9, 

* Para desplegar el API se usara un servidor web en flask

* Para consumo de los clientes se usara un Dash realizado en Dash Pyplot.

* Guias  de consumo de librearia [Binance](https://python-binance.readthedocs.io/en/latest/).

* Para el calculo de las predicciones se usaran las caracteristicas mas relevantes de cada uno de los klines por minutos extraidos del api, adicionalmente se calculara un valor VWAP que permitira al modelo predecir con mayor presicion los datos.

* Para el despligue y trabajar de forma colaborativa se usara un servidor ubuntu en la infraestructura de google cloud, donde se almacenaran todos los documentos y programas necesarios para el despliegue del modelo y sus servicos de consumo.
* Para extraer los datos de forma recurrente  se usara una tarea programada en el servidor a traves de un crontab

```sh
````
