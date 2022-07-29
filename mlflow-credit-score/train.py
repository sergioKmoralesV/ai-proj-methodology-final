import os
import warnings
import sys
import pandas as pd
import numpy as np
from creditscore.train import eval_metrics, data_split
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the csv file
    csv_path = "../data/train.csv"
    try:
        data = pd.read_csv(csv_path)
    except Exception as e:
        logger.exception(
            "Unable to download training & test CSV. Error: %s", e)

    data = data[["Interest_Rate", "Credit_Score"]]
    data_x = data.drop(["Credit_Score"], axis=1)
    data_y = data[["Credit_Score"]]

    # Split the data into training and test sets. (0.7, 0.3) split.
    train_x, test_x, train_y, test_y = data_split(data_x, data_y)

    n_estimators = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 3

    with mlflow.start_run():
        # Execute ElasticNet
        rf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        rf.fit(train_x, train_y)

        # Evaluate Metrics
        predicted = rf.predict(test_x)
        metrics = eval_metrics(test_y, predicted)
        # Print out metrics
        print("Random Forest model (n_estimators=%f, max_depth=%f):" % (n_estimators, max_depth))
        print("  Precision: %s" % metrics['precision'])
        print("  Recall: %s" % metrics['recall'])
        print("  Accuracy: %s" % metrics['accuracy'])
        print("  F1: %s" % metrics['f1'])

        # Log parameter, metrics, and model to MLflow
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("precision", metrics['precision'])
        mlflow.log_metric("recall", metrics['recall'])
        mlflow.log_metric("accuracy", metrics['accuracy'])
        mlflow.log_metric("f1", metrics['f1'])
        mlflow.sklearn.log_model(rf, "model")
