SHELL=/bin/bash

data_acquisition:
	@echo "Adquiriendo datos"
	source env_vars.env && ./scripts/data_acquisition/main.py

preprocessing:
	@echo "Preprocesando datos"
	source env_vars.env && .scripts/preprocessing/main.py

training:
	@echo "entrenamiento del modelo de datos"
	source env_vars.env && .scripts/training/main.py

Evaluariong:
	@echo "evaluacion del modelo"
	source env_vars.env && .scripts/evaluation/main.py

Visualization:
	@echo "visualizar dashboard"
	source env_vars.env && .scripts/visualization/dash_app.py

