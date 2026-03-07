import pandas as pd
from xgboost import XGBRegressor
from Berlin_House_Price_Prediction.config.configuration import ModelTrainerConfig
from Berlin_House_Price_Prediction import logger
import os
import joblib

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        try:
            # Load the training data
            train_data = pd.read_csv(self.config.train_data_path)
            X_train = train_data.drop(columns=[self.config.target_column.name])
            y_train = train_data[self.config.target_column.name]

            # Load the test data
            test_data = pd.read_csv(self.config.test_data_path)
            X_test = test_data.drop(columns=[self.config.target_column.name])
            y_test = test_data[self.config.target_column.name]

            # Initialize the model with parameters from params.yaml
            model = XGBRegressor(
                n_estimators=self.config.n_estimators,
                learning_rate=self.config.learning_rate,
                random_state=self.config.random_state
            )

            # Train the model
            model.fit(X_train, y_train)

            # Save the trained model
            model_path = os.path.join(self.config.root_directory, self.config.model_name)
            joblib.dump(model, model_path)
            logger.info(f"Model trained and saved at {model_path}")

        except Exception as e:
            logger.error(f"Error during model training: {e}")
            raise e