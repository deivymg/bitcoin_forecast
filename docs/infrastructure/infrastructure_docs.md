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
* Web Server  Flask. \Este servidor se uso para desplegar el dashboard
* Environment configuration \se usaron las herramientas para confirar el entorno ejecucion python 3.9, pyenv, poetry, jupyter.
* Execution pipelines con crontab.\
![image](https://user-images.githubusercontent.com/21108295/146661931-1d4592dd-aa06-4bff-8895-62a45dd3bc1f.png)


