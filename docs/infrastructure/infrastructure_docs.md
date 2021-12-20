# Infrastructure

a continuacion se describe la infraestructura usada para el despliegue del proyecto

* Maquina virtual .\
OS: Ubuntu 20.04.3 LTS x86_64\
Host: Google Compute Engine\
Kernel: 5.11.0-1022-gcp\
Uptime: 26 days, 16 hours, 4 mins\
Packages: 825 (dpkg), 6 (snap)\
Shell: bash 5.0.17\
Terminal: /dev/pts/4\
CPU: Intel Xeon (2) @ 2.199GHz\
Memory: 260MiB / 3928MiB\
En este servidor se realizo obtencion, procesamiento de datos, diseno y despliegue del modelo de prediccion.
\Tambien se uso para obtencion de datos en tiempo real del api de binance.
* Notebooks Google Colab: \se uso notebooks de google colab para desplegar servicios de dash  algunos servicios consumidos por la aplciacion como lo es la limpieza de los datos.
* Web Server  Flask. \Este servicio se uso para desplegar el API que consumen los clientes.
* HEROKU para desplegar la API de forma publica. 
* Dash. Este servicio se uso para desplegar el dashboard que consumen los clientes
* Repositorio de aplicacion Github, para trabajar colaborativamente y desarrollar la solucion
* Versionamiento del codigo Git.
* Environment configuration \se usaron las herramientas para confirar el entorno ejecucion python 3.9, pyenv, poetry, jupyter.
* Execution pipelines con crontab.\
![image](https://user-images.githubusercontent.com/21108295/146690530-917f60a0-c84b-416f-9c6c-7a54455426d7.png)

## Pasos dentro del despliegue final.

* Carga los datos mediante a API de binance de los ultimos 15 minutos.
* Preprocesa los datos y los carga en un path conocido.
* Carga los modelos pre entrenados desde un path conocido. 
* Realiza las predicciones los modelos con los datos preprocesados y los muestra en la API. 

![image](https://github.com/deivymg/bitcoin_forecast/blob/master/modelo1.jpeg)

![image](https://github.com/deivymg/bitcoin_forecast/blob/master/modelo2.jpeg)

Para mas informacion ver [despliegue_flask](https://github.com/deivymg/bitcoin_forecast/blob/master/scripts/api/main.py)



