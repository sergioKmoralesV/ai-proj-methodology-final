# AI project methodology - Credit score prediction


## To create new environment 
	$ conda env create -f conda.yaml
	
## To activate this environment, use
	$ conda activate cred-score

## To deactivate an active environment, use
	$ conda deactivate

## Activate MLflow UI
	$ mlflow ui --backend-store-uri mlflow-credit-score/mlruns
	
### View it at http://localhost:5000

## Run MLflow Packing Training Code in conda Environment
	$ cd mlflow-credit-score
	$ mlflow run mlflow-credit-score .

