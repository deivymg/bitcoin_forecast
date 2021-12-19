# Exit Report of Project <X> for Customer <Y>


	
Una vez se elaboro el modelo se definieron metricas para evaluar el desempeño con base en las siguientes mediciones y asi crear un despliegue que pueda ser consumido por el cliente mediante un API y un dashboard

	
##	Overview

Nuestra solucion calcula en tiempo real los rendimientos de la criptomoneda Bitcoin para los proximos 15 minutos, por lo cual puede usarse esto como un modelo de prediccion que le permitira a traders predecir el posible comportamiento de la criptomoneda durante los proximos 15 minutos y asi tomar una desicion de inversion con esta información.


##	Business Domain

Este modelo esta enfocado en proveer una solucion en tiempo real para traders e inversionistas en la criptomoneda bitcoin, con la cual podran hacer uso de uno modelo de deep learning basado en redes recuerrentes probado y validado para la prediccion de estas criptomonedas.

##	Business Problem

El problema que se busca resolver con esta solución es tener un criterio mas al momento de invertir en la criptomoneda bitcoin con el fin de que se pueda tener mas certeza sobre inversiones en este mercado tan volatil.

##	Data Processing
Los datos fueron tomados de un fuente abierta y procesados para determinar valores faltantes y outliers que puedieran afectar el entremaiento del modelo.

##	Modeling, Validation
Las tecnicas usadas para 
##	Solution Architecture

		* Mean Square Error: representa la media de la diferencia al cuadrado entre los valores originales y los predichos en el conjunto de datos. Mide la varianza de los residuos. 
	* Mean absolute error: representa la media de la diferencia absoluta entre los valores reales y los predichos en el conjunto de datos. Mide la media de los residuos en el conjunto de datos.
	* Root-mean-square deviation: Mide la varianza de los residuos.
	* R2: es la proporción de la variación de la variable dependiente que es predecible a partir de la variable independiente
	

El modelo se diseño para predecir los proximos el target el cual es el log residual de los rendimientos predecidos para los proximos 15 minutos, por lo cual la evaluacion sera sobre el valor de target predicho por nuestro modelo.
	
Las mediciones que se obtuvieron para este modelo son las siguientes.
	
	* Evaluation metric results:-
	* MSE is : 4.3382098817287355e-06
	* MAE is : 0.0014370301978646467 
	* RMSE is : 0.0020828369791533697
	* R2 is : -0.3962299464998571 
	

##	Benefits
	
###	Company Benefit (internal only. Double check if you want to share this with your customer)

	Los beneficios para nuestros clientes es contar con un modelo que le permita maximizar sus inversiones sobre la criptomoneda permitiendoles tener mayor certeza del futuro de sus inversiones a corto plazo (15 minutos), y de esta forma generar mayor rentabilidad al momento de invertir en esta criptomoneda.
	

###	Customer Benefit

	Este modelo permite incrementar en un 10 % las ganacias al invertir en esta criptomoneda puediendo determinar si el comportamiento de una criptomoneda espera crecer o decrecer en los proximos 15 minutos.

##	Learnings

### 	Project Execution
	
	Durante el desarrollo del proyecto se pudieron identifcar aquellas caracteristicas que le permiten a un modelo determinar si la criptomoneda esta al alza o por el contrario esta decrecera en los proximos 15 minutos, esto es un hito importante en el desarrollo de este proyecto.

### Data science / Engineering
	
	Un calentamiento por 5 epocas y un entrenamiento posterior con un menor learning rate, asi como un droput del 20% mejoro notablemente el desempeño de las predicciones de los modelos basados en redes recurrentes.
	
### Domain


### Product

Durante el desarrollo se probaron varias tecnologias como Airflow, pero despues de muchas fallas se decidio trabajar co teclogias mas sensillas e integradas como crontab a nivel de servidor.
	
Tambien encontramos muy ultil el estandarizar las salidas y entradas del modelo para asi poder usar diferentes fuentes de datos, aunque esto requirio mucho trabajo, permitio agilizar el proceso de despliegue del modelo.

###	What's unique about this project, specific challenges

	Los retos mas interesantes de este proyecto fue elaborar una solucion de principio a fin , desde configurar servidor, desarrollar el modelo, construir clases y usar librerias especializadas, hasta el despliegue de la solucion en API y dashboard lo que permite a los clientes consumir de varias formas el servicio hizo que este proyecto fuera muy interesante y que cubriera a nivel generar todo lo requierido para manejar proyectos de sicencia de datos.

##	Links
	* [Calculo de VWAP] (https://www.rankia.com/blog/bolsa-desde-cero/4279449-que-como-utiliza-vwap) usado por nuestro modelo para estandarizar las entradas a nuestro model.
	* [Best models to predict Cryptocurrenci prices](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwj07ujYgvH0AhXwSzABHfdSAUgQFnoECAYQAQ&url=https%3A%2F%2Fwww.mdpi.com%2F2673-2688%2F2%2F4%2F30%2Fpdf&usg=AOvVaw0KhCNFL1bCA5WnrzmjXV5G)
	* [Building a predictive model for cryptocurrencies investment ](https://miuc.org/building-a-predictive-model-for-cryptocurrencies-investment/)
	

##	Next Steps
 
Los proximos pasos para nuestro proyecto es adicoinar mas activos para que nuestro modelo pueda ser extrapolado a otras criptomonedas.
	
## Appendix

	#Funcionamiento del dashboard
	
![image](https://user-images.githubusercontent.com/21108295/146695026-b47d05fa-dbbe-4e76-af88-3feec6bd4264.png)

	#Funcionamiento del API
	
![image](https://user-images.githubusercontent.com/21108295/146695236-0cc68457-f0c9-47ce-8125-d4fda053fedf.png)

	
	
