# Deployment

* Para desarrollar el modelo se usara un entorno de cofiguracion con pyenv y configurado con las indicaciones que encontrar en el archivo [Makefile](https://github.com/deivymg/bitcoin_forecast/blob/master/Makefile)

* La elaboración de los modelos de prediccion se usara python 3.9, 

* Para desplegar el API se usara un servidor web en flask

* Para consumo de los clientes se usara un Dash realizado en Dash Pyplot.

* Para el consumo de los modelos, se creara una api a travez de Flask y luego se desplegara de forma publica mediante Heroku. 

* Guias  de consumo de librearia [Binance](https://python-binance.readthedocs.io/en/latest/).

* Para el calculo de las predicciones se usaran las caracteristicas mas relevantes de cada uno de los klines por minutos extraidos del api, adicionalmente se calculara un valor [VWAP](https://github.com/deivymg/bitcoin_forecast/blob/master/docs/data/vwap.md) que permitira al modelo predecir con mayor presicion los datos.

* Para el despligue y trabajar de forma colaborativa se usara un servidor ubuntu en la infraestructura de google cloud, donde se almacenaran todos los documentos y programas necesarios para el despliegue del modelo y sus servicos de consumo.
* Para extraer los datos de forma recurrente  se usara una tarea programada en el servidor a traves de un crontab que ejecuta el programa de data_adquisition cada minuto.

```sh
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
* * * * * export BINANCE_RAW_PATH="${HOME}/bitcoin_forecast/scripts/data_acquisition/data/raw/"; /usr/bin/python3 /home/superequipo/bitcoin_forecast/scripts/data_acquisition/main.py >> /home/superequipo/api.log 2>&1
````
