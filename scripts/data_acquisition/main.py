
import os
import pandas as pd
import binance
from binance.client import Client


#inicializamos las claves
binance_api=os.environ.get('BINANCE_API')
binance_secret=os.environ.get('BINANCE_SECRET')

client = Client(binance_api, binance_secret)

#solicitamos los datos por minuto iniciando desde los ultimos 15 minutos

timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '15m')
bars = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, "15 minutes ago UTC")
#eliminamos atributos no necesarios
for line in bars:
    del line[5:]
    
#convertimos los datos a un dataframe
bars = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, "15 minutes ago UTC")

btc_df = pd.DataFrame(bars, columns=['timestamp',
                                    'Open',
                                    'High',
                                    'Low',
                                    'Close',
                                    'Volume',
                                    'Close time',
                                    'Close time',
                                    'Count',
                                    'Taker buy base asset volume',
                                    'Taker buy quote asset volume',
                                    'Ignore'])
#eliminamos columnas que no sirven y reordenamos los datos
btc_df = btc_df[['timestamp','Count', 'Open', 'High', 'Low', 'Close', 'Volume' ]]
btc_df ['timestamp'] = btc_df['timestamp'].astype(str)
btc_df ['timestamp'] = btc_df['timestamp'].str[:11]
btc_df.set_index('timestamp', inplace=True)

btc_df.to_csv('ultimos_15_minutos.csv')
