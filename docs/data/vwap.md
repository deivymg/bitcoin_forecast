# Calculo VWAP

El calculo del vwap se hizo basado en la siguiente formla

![image](https://user-images.githubusercontent.com/21108295/146661310-317af9e5-7f61-4cdc-8e56-0c28316240a2.png)

para lo primero se obtuvieron todos extraidos de las ultimas 24 horasa bwap se calcula a partir de la primera transaccion hasta un calculo promedio de todas las transacciones hechas hasta el punto actual.

```python
bars = client.get_historical_klines('BTCUSDT', 
                                    Client.KLINE_INTERVAL_1MINUTE, 
                                    "1 day ago UTC")
```
como solo sirven los datos del dia debemos filtrar las ultimas 24 horas para que solo traiga los que nos interesan

```python
fechahoy = str(datetime.now().date())
fechamanana = str(datetime.now().date() + timedelta(days=1) )
btc_df=btc_df.loc[totimestamp(fechahoy):totimestamp(fechamanana)-1]
```

posteriormente se calcula la formula usando pandas para no usar un for, por lo tanto se crean columnas y se hace el calculo
```python
btc_df['TypicalPrice'] = (btc_df['High']+btc_df['Low']+btc_df['Close'])/ 3
btc_df['sumTypicalPrice'] = btc_df.TypicalPrice.cumsum()
btc_df['sumVol'] = btc_df.Volume.cumsum()
btc_df ['VWAP'] = (btc_df['sumTypicalPrice'] * btc_df['Volume'])/ btc_df['sumVol']
```

puede ver el script <a href='https://github.com/deivymg/bitcoin_forecast/blob/master/scripts/data_acquisition/main.py'>aqui</a>
