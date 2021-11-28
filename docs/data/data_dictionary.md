# Diccionario de datos

# Transacciones Históricas

Este conjunto de datos contiene información sobre transacciones históricas para varios criptoactivos, como Bitcoin y Ethereum. Estos datos son extraidos desde kaggle en https://www.kaggle.com/c/g-research-crypto-forecasting/data.


## Tabla 1


| column | type | description |
| --- | --- | --- |
| timestamp | int64 | timestamp por cada minuto. |
| Count | in64 | número de tranzaciones durante el minuto. |
| Asset_ID | float64 | Codigo ID de una criptomoneda. |
| Open | float64 | Precio al comienzo del minuto. |
| High | float64 | Precio máximo alcanzado durante el minuto. |
| Low | float64 | Precio mínimo alcanzado durante el minuto |
| Close | float64 |  Precio al final del minuto. |
| Volume | float64 | Número de criptomonedas tranzadas .durante el minuto.|
| VWAP | float64| Volume weighted average price. Precio promedio al que se comerció la criptomoneda. |
| Target | float64 | Residual log-returns para la cripto moneda durante los próximos 15 mins.|


