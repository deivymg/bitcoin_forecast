# Project Charter

## Business background

* El cliente de este proeyecto es la firma de inversiones DelaPava & Co Inc. con sede en la ciudad de bogotá.
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
		* 		contacto: marentesk@gmail.com 
	* Client:
		* Melissa De La Pava Rodriguez
		* 		 contacto: medel@unal.edu.co
	
## Metrics
* Se elige desarrollar el proyecto seguiendo metodologias agiles, SCRUM.
* Metricas de Sprint, Work Burndown Chart, Sprint restrospective
* Desarrollo de aplicacion para la prediccion del comportamiento de acciones y criptomonedas.
* Retroalimentacion del cliente
* Criterio de aceptacion del proyecto

* Para la medición del rendimiento de los modelos propuestos se utilizara:
<ol>
	<li>Error medio (ME – Mean Error)</li>
	<li>Error absoluto medio (MAE – Mean Absolute Error )</li>
	<li>Error cuadrático medio (MSE – Mean Square Error)</li>
	<li>La raíz del error cuadrático medio (RMSE – Root Mean Square Error)/li>
	<li>Error porcentual medio (MPE – Mean Percentage Error )</li>
	<li>Error porcentual absoluto medio (MAPE – Mean Absolute Percentage Error)</li>
</ol>







## Plan
* Milestones
* 	Crear libreria para consumo de API de YahooFinance
* 	Crear libreria para consumo de API de criptomonedas
* 	Exploracion de datos de las APIs
* 	Diseñar un DataStream 
* 	Diseñar arquitectura para alamaacenar los datos obtenidos
* 	Definir flujo de tareas y frecuencia con la que se van a consumir los datos de las APIs
* 	
* 	Modelado de series de tiempo
* 	Elegir un modelo de prediciones de series de tiempo
* 	Crear API de microservicio para consumir el modelo elegido
* 	Diseño de interfaz de usurio
* 	Entregar el proyecto
* 	

## Architecture
* Data
  * Datos estructurados en CSV
  * Se cosumen los datos de las APIs de Yahoo Finance y Binance
  * 	 https://pypi.org/project/yfinance/
  * 	 https://python-binance.readthedocs.io/en/latest/
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * Python pandas para exploracion de los datos
  * Python TensorFlow para modelado y prediccion
  * Django/Flask para la implementacion del API
  * Docker	
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* La comunicacion entre los stakeholders y los miembros del equipo será por los siguinetes medios:
* Mensajeria instantanea Whatsapp
* Correo electrónico
* Tablero de tareas en trello
* 	 https://trello.com/b/L4oX6qe9/proyectodsml6prediccionbolsacripto

