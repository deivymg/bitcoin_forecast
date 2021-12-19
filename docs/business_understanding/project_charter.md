# Project Charter

## Business background

* El cliente de este proyecto es la firma de inversiones DelaPava & Co Inc. con sede en la ciudad de bogotá.
*  DelaPava & Co esta buscando en invertir en herramientas de analítica que le ayude a su equipo de inversiones a hacer predicciones en el mercado de la criptomonedas y del precio de acciones de empresas en la bolsa de Nueva York.

## Scope
* Implementar modelo de prediccion de series de tiempo.
* Aplicacion web para consumir el modelo.
* Será consumida mediante un formulario en una pagina web donde el usuario final podrá elegir una acción o critomoneda y se otendrá una gráfica con predicciones de series de tiempo

## Personnel
* El equipo de este proyecto son los intergandes del grupo superequipo del curso Ciencia de datos y Machine Learning Avanzado de la Universidad Nacional de Colombia, 2021
	* SuperEquipoDataSolutions:
		* Project lead
		* 	* Deivy Martinez
		* 		contact: deivymg@gmail.com
		* PM
		* 	* Edwin Perez
		* 		contacto: edwinaperez32@gmail.com
		* Data scientist(s)
		*	* Christian Otero
		*		contacto: criscotero@gmail.com 	
		* Account manager
		* 	* David Reyes
		* 		contacto: da.reyes19996@gmail.com
	* Cliente:
		* Melissa De La Pava Rodriguez, Gerente DelaPava & Co Inc
		* 		 contacto: medel@unal.edu.co
	
## Metrics
* Se elige desarrollar el proyecto seguiendo metodologias agiles, SCRUM.
* Metricas de Sprint, Work Burndown Chart, Sprint restrospective
* Desarrollo de aplicacion para la prediccion del comportamiento de acciones y criptomonedas.
* Retroalimentacion del cliente
* Criterio de aceptacion del proyecto

* Mejorar la rentabilidad promedio al momento de realizar una transacción.
* proporcionar información acerca del pronostico de la criptodivisa.

* Para la medición del rendimiento de los modelos propuestos se utilizara:
<ol>
	<li>Error medio (ME – Mean Error)</li>
	<li>Error absoluto medio (MAE – Mean Absolute Error )</li>
	<li>Error cuadrático medio (MSE – Mean Square Error)</li>
	<li>La raíz del error cuadrático medio (RMSE – Root Mean Square Error)</li>
	<li>Error porcentual medio (MPE – Mean Percentage Error )</li>
	<li>Error porcentual absoluto medio (MAPE – Mean Absolute Percentage Error)</li>
</ol>




## Plan

* Business Understanding
* 	Reconocimiento del modelo de negocio
* 	Definicion del As-Is
* 	Definicion del To-Be
* 	
* Data Undestanding
* 	Reconocimiento de los datos
* 	Recuperación de datos
* 		Crear libreria para consumo de API de YahooFinance
* 		Crear libreria para consumo de API de criptomonedas
* 	 	Exploracion de datos de las APIs
* 		Diseñar un DataStream 
* 		Diseñar arquitectura para almacenar los datos obtenidos
* 		Definir flujo de tareas y frecuencia con la que se van a consumir los datos de las APIs
* 	Exploración de los datos
* 	Limpieza de datos

* Modeling
* 	Investigación de modelos existentes
* 	Creación del modelo
* 		Modelado de series de tiempo
* 		Elegir un modelo de prediciones de series de tiempo
* 		Consumir un microservicio API para implementacion del modelo elegido
* 	Evaluacion del modelo
* 	Creacion de Dashboard
* 		Diseño de interfaz de usuario
* Deployment
* 	Importe del proyecto
* 	Prueba de Concepto del proyecto
* 	Evaluacion del PM
* 	Entrega Final a Pettite Comitté
* 	Puesta en ambiente de Certificación
* 	Prueba de Usuario Final

* 
* Acceptance
* 	Puesta en Producción
* 	Evaluacion del Usuario Final
* 	Entregar el proyecto
* 	

## Architecture
* Data
  * Datos estructurados en CSV
  * Para el despligue se usara un APi en flash y un Dashboard en python con Dash
  * Tambien se realizara un consumo de los datos con un api en python con la librearia de binance python.
  * Toda la comunicacion sera a traves de un servidor cloud en google donde se diseñara y desplegara el modelo de predicción
  * Tambien se entrenara el modelo con un dataset publico en kaggle que tiene datos suficientes para entrenar nuestro modelo. 
  * Se trabajará con la siguiente informacion respecto a una accioón o criptomoneda

<ol>
<li>Previous Close</li>
<li>Open</li>
<li>High</li>
<li>Low</li>
<li>Volume</li>
<li>Avg. Volume</li>
</ol>


* Movimiento de datos a traves de un Crom de Linux para la ejecucuión de un programa de python para pre-procesamiento de datos.



* What tools and data storage/analytics resources will be used in the solution e.g.,
  * Python pandas para exploracion de los datos
  * Python TensorFlow para modelado y prediccion
  * Django/Flask para la implementacion del API
  * dash plotly/python para generacion de dashboard 
  
 
 


## Communication
* La comunicacion entre los stakeholders y los miembros del equipo será por los siguinetes medios:
* Mensajeria instantanea Whatsapp 
* Correo electrónico
* Tablero de tareas en trello
* 	 https://trello.com/b/L4oX6qe9/proyectodsml6prediccionbolsacripto
* Se realizarán reuniones cada dos (2) días definidos por el sprint

