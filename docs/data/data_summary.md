# Data Report

los datos son extraidos a traves de la web API de Binance, esta nos ofrece los datos de la criptomoneda en cuestion (BITCOIN).
primero se genera un request a la API para que nos enterge la informacion del historico de BITCOIN en un periodo de 15min.
la respuesta de la API nos entrega una lista con los valores de fecha (data_stamp), apertura(Open), Alto(High), bajo(Low) y cierre(Close)

## General summary of the data

los datos al ser de valores de la criptomoneda, son de caracter numerico indicando el precio de la criptodivisa en el momento de su transaccion

## Data quality summary

los datos obtenidos por la API estan completos, sin valores nulos ni vacios.

## Target variable

Las variables objetivo que tienen un mayor peso en el modelo son:

1. Open
2. Close

## Individual variables

Las variables entregadas por la API son:

1. Open
2. High
3. Low
4. Close
5. Date

## Variable ranking

la mejor clasificación que le podemos dar a las variablems de foma Ordinal es la siguiente:

1. Close
2. Open
3. Date
4. High
5. Low

## Relationship between explanatory variables and target variable

la relación que existe entre las variables es bastante alta ya que determinan el comportamiento de la criptodivisa.

para mayor información dirijase a la carpeta ../scripts/eda/eda.py
