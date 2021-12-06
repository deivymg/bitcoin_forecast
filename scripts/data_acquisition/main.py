import os
import pandas as pd
from binance.client import Client


#inicializamos las claves
binance_api='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
binance_secret='xxxxxxxxxxxxxxxxxxxxxxxxxx'


client = Client(binance_api, binance_secret)

#solicitamos los datos por minuto iniciando desde los ultimos 15 minutos

timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '15m')
bars = client.get_historical_klines('BTCUSDT', '1m', timestamp, limit=1000)

#eliminamos atributos no necesarios
for line in bars:
    del line[5:]
    
#convertimos los datos a un dataframe
btc_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
btc_df.set_index('date', inplace=True)
btc_df.to_csv('ultimos 15 minuts.csv')
