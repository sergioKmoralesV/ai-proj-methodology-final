# AI project methodology - Credit score prediction
### Team members 👥
- Sergio Morales
- Isaac Gonzales




## To create new environment 
	$ conda env create -f conda.yaml
	
## To activate this environment, use
	$ conda activate cred-score

## To deactivate an active environment, use
	$ conda deactivate

# MLflow

## Activate MLflow UI
	$ mlflow ui --backend-store-uri mlflow-credit-score/mlruns
	
### View it at http://localhost:5000

## Run MLflow Packing Training Code in conda Environment
	$ cd mlflow-credit-score
	$ mlflow run mlflow-credit-score .

## Deploy the Model Using MLflow Models through a REST API

	$ mlflow models serve --model-uri mlflow-credit-score/mlruns/0/4524303c575b408ea41da2dc4422ffb5/artifacts/model -p 1234

