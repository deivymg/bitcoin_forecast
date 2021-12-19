

import os
import pandas as pd
from binance.client import Client
import numpy as np
import time
from datetime import datetime, timedelta


def main():
    #inicializamos las claves
    binance_api=os.environ['BINANCE_API']
    binance_secret=os.environ['BINANCE_SECRET']
    #cargamos el ciente para consulta del api
    client = Client(binance_api, binance_secret)
    
    #solicitamos los datos agrupados por minuto iniciando desde los ultimos 15 minutos  
    bars = client.get_historical_klines('BTCUSDT', 
                                    Client.KLINE_INTERVAL_1MINUTE, 
                                    "1 day ago UTC")
    
    #Cargamos solo las columnas necesarias
    
    
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
    #función para convertir fechas en string a timestamp para poder filtrar los datos
    totimestamp = lambda s: np.int32(time.mktime(datetime.strptime(s, "%Y-%m-%d").timetuple()))
                                  
    #eliminamos columnas que no sirven y reordenamos los datos
    btc_df = btc_df[['timestamp','Count', 'Open', 'High', 'Low', 'Close', 'Volume' ]]
    btc_df ['timestamp'] = btc_df['timestamp'].astype(str)
    btc_df ['timestamp'] = btc_df['timestamp'].str[:10]
    btc_df ['timestamp'] = btc_df['timestamp'].astype(int)
    #ordenamos los valores en orden ascendente
    btc_df.sort_values(by=['timestamp'])
    btc_df ['High'] = btc_df['High'].astype(float)
    btc_df ['Low'] = btc_df['Low'].astype(float)
    btc_df ['Close'] = btc_df['Close'].astype(float)
    btc_df ['Volume'] = btc_df['Volume'].astype(float)
    btc_df.set_index('timestamp', inplace=True)
    
    #obtenemos en formato timestamp los datos necesarios para calcular el vwap diario
    fechahoy = str(datetime.now().date())
    fechamanana = str(datetime.now().date() + timedelta(days=1) )
    btc_df=btc_df.loc[totimestamp(fechahoy):totimestamp(fechamanana)-1]
    
    #calculamos las columnas necesarias para el vwap
    btc_df['TypicalPrice'] = (btc_df['High']+btc_df['Low']+btc_df['Close'])/ 3
    btc_df['sumTypicalPrice'] = btc_df.TypicalPrice.cumsum()
    btc_df['sumVol'] = btc_df.Volume.cumsum()
    
    #calculamos el vwap y el target en 0
    btc_df ['VWAP'] = (btc_df['sumTypicalPrice'] * btc_df['Volume'])/ btc_df['sumVol']
    btc_df ['Target'] = 0
    
    #eliminamos columnas no cesarias antes de guardar el archivo
    btc_df.drop(['sumVol', 'sumTypicalPrice', 'TypicalPrice'], axis=1,inplace=True)
    
    # path para guardar el archivo
    save_data_path =os.path.join(os.environ['BINANCE_RAW_PATH'],'ultimos_15_minutos.csv')
    
    #guardamos el dataframe en un archivo en formato csv
    btc_df.to_csv(save_data_path)

  
if __name__=="__main__":
    main()

