SHELL=/bin/bash

data_acquisition:
	source env_vars.env && ./scripts/data_acquisition/main.py
