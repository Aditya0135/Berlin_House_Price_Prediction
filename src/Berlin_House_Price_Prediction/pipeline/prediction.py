import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

    def preprocess(self,data):
        # Implement any necessary preprocessing steps here
        """
        input_dict example:
        {
            'zipcode': 10115,
            'heating': 'Gas',
            'energy': 'Gas',
            'area': 100,
            'rooms': 3
        }
        """
        # Convert dict to dataframe
        df = pd.DataFrame([data])

        # One-hot encode categorical features
        cat_features = ['zipcode', 'heating', 'energy']  # all categorical
        encoded = self.encoder.transform(df[cat_features])
        encoded_df = pd.DataFrame(
            encoded,
            columns=self.encoder.get_feature_names_out(cat_features)
        )

        # Drop original categorical columns and concat encoded
        df = df.drop(columns=cat_features)
        df = pd.concat([df, encoded_df], axis=1)

        # Ensure all columns match training set
        for col in self.feature_columns:
            if col not in df.columns:
                df[col] = 0  # add missing columns as 0

        # Keep only the columns in the same order as training
        df = df[self.feature_columns]

        return df

    def predict(self, data):
        data = self.preprocess(data)
        prediction = self.model.predict(data)
        return prediction