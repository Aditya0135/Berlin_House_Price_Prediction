import joblib
import numpy as np
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
        self.scaler = joblib.load(Path("artifacts/data_transformation/scaler.joblib"))
        self.columns = list(self.model.feature_names_in_)
        self.index_dict = dict(zip(self.columns, range(len(self.columns))))

    def create_vector(self, zipcode, area, rooms, energy, heating):
        new_vector = np.zeros(len(self.columns))

        # numeric features
        if "rooms" in self.index_dict:
            new_vector[self.index_dict["rooms"]] = rooms

        if "area" in self.index_dict:
            new_vector[self.index_dict["area"]] = area

        # categorical features
        if energy in self.index_dict:
            new_vector[self.index_dict[energy]] = 1

        if heating in self.index_dict:
            new_vector[self.index_dict[heating]] = 1

        if zipcode in self.index_dict:
            new_vector[self.index_dict[zipcode]] = 1

        return new_vector.reshape(1, -1)

    def predict(self, data):
        # extract scalar values from DataFrame
        rooms = data["rooms"].iloc[0]
        zipcode = data["zipcode"].iloc[0]
        area = data["area"].iloc[0]
        energy = data["energy"].iloc[0]
        heating = data["heating"].iloc[0]

        x = self.create_vector(zipcode=zipcode, area=area, rooms=rooms,
                               energy=energy, heating=heating)
        
        # scale only numeric features (example: area, rooms)
        numeric_idx = [self.index_dict["area"], self.index_dict["rooms"]]
        x[0, numeric_idx] = self.scaler.transform(x[0, numeric_idx].reshape(1, -1))
        
        return self.model.predict(x)