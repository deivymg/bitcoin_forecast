from pydantic import  BaseModel

class BinanceCredential(BaseModel):
	"""
	Class for  Binance Connection

	Attributes
	------------

	binance_api : str
		 token of binance for client info

	binance_secret : str
		 token of binance for client info

	"""
	binance_api : str
	binance_secret : str

