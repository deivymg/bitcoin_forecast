import os
from packagename.datamodels.environment import BinanceCredential

def get_binance_credenctial() -> BinanceCredential:
        """
        Funcion to get Binance Credentials
        Returns
        ........

        credential: BinanceCredential
                Object with binance credentials
        """
        credential = BinanceCredential(

                        binance_api=os.environ['BINANCE_API']
                        binance_secret=os.environ['BINANCE_SECRET']

                        )
        return credential


