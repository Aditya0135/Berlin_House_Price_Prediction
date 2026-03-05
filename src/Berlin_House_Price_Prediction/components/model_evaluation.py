import os
import pandas as pd
from pathlib import Path
from Berlin_House_Price_Prediction.entity.config_entity import ModelEvaluationConfig
from Berlin_House_Price_Prediction.utils.common import save_json
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred)->bool:
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop(self.config.target_column, axis=1)
        y_test = test_data[self.config.target_column]


        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(self.config.mlflow_uri).scheme

        with mlflow.start_run():
            
            predicted_prices = model.predict(X_test)
            (rmse, mae, r2) = self.eval_metrics(y_test, predicted_prices)
            
            # saving metrics to local file
            score = {
                "rmse": rmse,
                "mae": mae,
                "r2_score": r2}
            
            save_json(path=Path(self.config.metric_file_name), data=score)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2_score", r2)

            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                # Register the model
                mlflow.sklearn.log_model(model, "model", registered_model_name="GradientBoostingRegressor")
            else:
                mlflow.sklearn.log_model(model, "model")
