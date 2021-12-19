SHELL=/bin/bash

data_acquisition:
	@echo "Adquiriendo datos"
	source env_vars.env && python3 scripts/data_acquisition/main.py

preprocessing:
	@echo "Preprocesando datos"
	source env_vars.env && python3 scripts/preprocessing/main.py

training:
	@echo "entrenamiento del modelo de datos"
	source env_vars.env && python3 scripts/training/main.py

evaluariong:
	@echo "evaluacion del modelo"
	source env_vars.env && python3 scripts/evaluation/main.py

visualization:
	@echo "visualizar dashboard"
	source env_vars.env && python3 scripts/visualization/dash_app.py 

