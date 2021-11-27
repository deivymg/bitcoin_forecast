# Project Charter

## Business background

* Who is the client, what business domain the client is in.
* What business problems are we trying to address?

## Scope
* Implementar modelo de prediccion de series de tiempo.
* Aplicacion web para consumir el modelo.
* How is it going to be consumed by the customer?

## Personnel
* Who are on this project:
	* SuperEquipoDataSolutions:
		* Project lead
		* 	* Deivy Martinez
		* PM
		* 	* Edwin Perez
		* Data scientist(s)
		*	* Christian Otero 	
		* Account manager
		* 	* David Reyes
	* Client:
		* Melissa De La Pava Rodriguez
		* Business contact: medel@unal.edu.co
	
## Metrics
* Desarrollo de aplicacion para la prediccion del comportamiento de acciones y criptomonedas.
* Se elige desarrollar el proyecto seguiendo metodologias agiles, SCRUM.
* Metricas de Sprint, Work Burndown Chart,= 
* Retroalimentacion del cliente
* Criterio de aceptacion del proyecto

## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.

## Architecture
* Data
  * Datos estructurados en CSV
  * Se cosumen los datos de las APIs de Yahoo Finance y Binance
  * 	* https://pypi.org/project/yfinance/
  * 	* https://python-binance.readthedocs.io/en/latest/
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* How will we keep in touch? Weekly meetings?
* Who are the contact persons on both sides?
