import os
import joblib
from Berlin_House_Price_Prediction.config.configuration import DataTransformationConfig
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        self.df = pd.read_csv(config.data_path)

        # Feature configuration
        self.features = config.features
        self.target = config.target
        self.numeric_features = config.numeric_features
        self.categorical_features = config.categorical_features
        self.scaler = StandardScaler()
    
    # -----------------------------
    # Cleaning
    # -----------------------------
    def clean_categorical_columns(self):
        """
        Clean categorical string columns:
        - strip whitespace
        - remove commas
        """
        categorical_cols = [col for col in self.categorical_features if col != "zipcode"]
        for col in categorical_cols:
            self.df[col] = self.df[col].str.strip().str.replace(',', '')

        # Special case cleaning
        if "energy" in self.df.columns:
            self.df["energy"] = self.df["energy"].str.replace(r"\s*offener", "", regex=True)  
    
    # -----------------------------
    # Category normalization
    # -----------------------------
    def remove_duplicate_categorical_columns(self):

        """
        Clean categorical string columns:
        - Merges synonymous heating and energy categories
        - Removes 
        """
        heating_map = {
            "Fußbodenheizung offener": "Fußbodenheizung",
            "Etagenheizung offener": "Etagenheizung",
            "Wärmepumpe offener": "Wärmepumpe",
            "Luft-/": "Wärmepumpe",
            "Wasser-": "Wärmepumpe",
        }
        energy_map = {
            'Luft-/': 'Wärmepumpe',
            'Fußbodenheizung': 'Andere',
            'Niedrigenergiehaus': 'Andere'
        }

        if "heating" in self.df.columns:
            # Merge synonymous 'heating' categories
            self.df["heating"] = self.df["heating"].replace(heating_map)

            # Merge rare 'heating' categories into 'Other'
            counts = self.df["heating"].value_counts()
            rare_categories = counts[counts < 48].index
            self.df["heating"] = self.df["heating"].replace(rare_categories, "Other")

        
        if "energy" in self.df.columns:
            # Merge synonymous 'energy' categories
            self.df["energy"] = self.df["energy"].replace(energy_map)

            # Merge rare 'energy' categories into 'Other'
            counts = self.df["energy"].value_counts()
            rare_categories = counts[counts < 20].index
            self.df["energy"] = self.df["energy"].replace(rare_categories, "Other")

    # -----------------------------
    # Outlier removal
    # -----------------------------
    def drop_outliers(self):
        """
            Drops about 2% of extreme data (100 rows)
        """
        q_low = self.df['price'].quantile(0.01)
        q_high = self.df['price'].quantile(0.99)

        self.df = self.df[(self.df['price']>q_low)&(self.df['price']<q_high)]
    # -----------------------------
    # Missing value imputation
    # -----------------------------
    def impute_missing_values(self):
        """
        Imputes categorical variables by the given probabilities
        """
        heating_top_categories = ['Zentralheizung', 'Gas', 'Fernwärme']
        energy_top_categories = ['Gas', 'Fernwärme', 'Wärmepumpe']
        probabilities_heating = [0.7, 0.15, 0.15]  
        probabilities_energy = [0.6, 0.3, 0.1]  

        self.df.loc[self.df['heating'] == 'na', 'heating'] = np.random.choice(
            heating_top_categories, 
            size=self.df[self.df['heating']=='na'].shape[0], 
            p=probabilities_heating
            )
        self.df.loc[self.df['energy'] == 'na', 'energy'] = np.random.choice(
            energy_top_categories,
            size=self.df[self.df['energy']=='na'].shape[0],
            p=probabilities_energy
            )
    # -----------------------------
    # Feature preparation
    # -----------------------------
    def prepare_features(self):
        """
        Select features and encode categorical variables
        """
        X = self.df[self.features].copy()
        X = pd.get_dummies(X, columns=self.categorical_features, drop_first=True)

        y = self.df[self.target]

        return X, y
    # -----------------------------
    # Train-test split
    # -----------------------------    
    def split_data(self, X, y):
        """
        Split dataset into train and test
        """
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        return X_train, X_test, y_train, y_test
    # -----------------------------
    # Scaling
    # -----------------------------    
    def scale_data(self, X_train, X_test):
        """
        Scale numeric features
        """
        X_train = X_train.copy()
        X_test = X_test.copy()

        X_train[self.numeric_features] = self.scaler.fit_transform(
            X_train[self.numeric_features]
        )

        X_test[self.numeric_features] = self.scaler.transform(
            X_test[self.numeric_features]
        )
        # save fitted scaler
        joblib.dump(self.scaler, "artifacts/data_transformation/scaler.joblib")
        return X_train, X_test
    
    def run_transformation_pipeline(self):
        """
        Complete transformation workflow
        """

        self.clean_categorical_columns()
        self.remove_duplicate_categorical_columns()
        self.drop_outliers()
        self.impute_missing_values()

        X,y = self.prepare_features()
        X_train, X_test, y_train, y_test= self.split_data(X,y)
        X_train, X_test = self.scale_data(X_train,X_test)

        train_df = pd.concat([X_train, y_train], axis=1)
        test_df = pd.concat([X_test, y_test], axis=1)

        train_df.to_csv(os.path.join(self.config.root_directory, "train.csv"), index=False)
        test_df.to_csv(os.path.join(self.config.root_directory, "test.csv"), index=False)
        return X_train, X_test, y_train, y_test