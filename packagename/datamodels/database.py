from pydantic import BaseModel

class DataLakePaths(BaseModel):
	"""

	Class for database data

	Attributes
	..........
	
	BTC_raw_df : str
		path to BTC database	
	preprocessed_data : str
		path to preprocessed data
	models : str	
		path to models
	"""
	BTC_raw_df : str
	preprocessed_data : str
	models : str

