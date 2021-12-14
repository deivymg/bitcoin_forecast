
# Liempieza y preprocesamiento

Luego de extraer los datos crudos del web API de Binance, estos se limpian y se les realiza un preprocesamiento.

## Limpieza

- Se eliminan filas en las que cualquier columna tenga NA.
- Se rellenan los datos para los minutos faltantes con el ultimo valor. 

## Preprocesamiento

Hacemos un preprocesamiento de los datos con la idea de implementar un modelo LSTM para regresion multivariable con una única salida. La cual será  nuestro target para los proximos 15 mins.

*Target* - Residual log-returns para la cripto moneda durante los próximos 15 mins.

- Se arma el data-set de entrada X el vector de salida Y
- Escojemos nuestro dataset datos del 2021 desde 2021-06-13T00:00:00 a 2021-09-20T23:44:00.
- Se estandarizan los datos. 
- Se prepara el dataset en el formato de entrada del módelo LSTM
- Se dividen los datos de la serie de tiempo en muestras consecutivas de n_steps unidades de tiempo


para mayor información dirijase a la carpeta ../scripts/preprocessing/preprocessing.py
