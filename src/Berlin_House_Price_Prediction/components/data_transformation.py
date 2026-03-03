from Berlin_House_Price_Prediction.config.configuration import DataTransformationConfig
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
                            #######################################
                            #                   TODO:             #
                            #   methods need updates to:          #
                            #   - standardize variables           #
                            #   - return self for chaining        #
                            #######################################
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
    
    
    def clean_categorical_columns(self):
        """
        Clean categorical string columns:
        - strip whitespace
        - remove commas
        """
        self.df['energy'] = self.df['energy'].str.strip().str.replace(',', '', regex=True)
        self.df['heating'] = self.df['heating'].str.strip().str.replace(',', '', regex=True)

        self.df['energy'] = self.df['energy'].str.strip()
        self.df['energy'] = self.df['energy'].str.replace(',', '', regex=False)
        self.df['energy'] = self.df['energy'].str.replace(r'\s*offener', '', regex=True)  
    

    def remove_duplicate_categorical_columns(self):

        """
        Clean categorical string columns:
        - Merges synonymous heating and energy categories
        - Removes 
        """
        self.df['heating'] = self.df['heating'].replace({
            'Fußbodenheizung offener': 'Fußbodenheizung',
            'Etagenheizung offener': 'Etagenheizung',
            'Wärmepumpe offener': 'Wärmepumpe',
            'Luft-/': 'Wärmepumpe',
            'Wasser-': 'Wärmepumpe'
        })
        # lets now merge categories having less then 50 obs to others
        counts = self.df['heating'].value_counts()
        other_categories = counts[counts < 48].index
        self.df['heating'] = self.df['heating'].replace(other_categories, 'Others')

        # Merge synonymous 'energy' categories
        energy_map = {
            'Luft-/': 'Wärmepumpe',
            'Fußbodenheizung': 'Andere',
            'Niedrigenergiehaus': 'Andere'
        }

        self.df['energy'] = self.df['energy'].replace(energy_map)

        counts = self.df['energy'].value_counts()
        rare = counts[counts < 20].index

        self.df['energy'] = self.df['energy'].replace(rare, 'Other')

    def drop_outliers(self):
        """
            Drops about 2% of extreme data (100 rows)
        """
        q_low = self.df['price'].quantile(0.01)
        q_high = self.df['price'].quantile(0.99)

        self.df = self.df[(self.df['price']>q_low)&(self.df['price']<q_high)]

    def impute_missing_values(self):
        """
        Imputes categorical variables by the given probabilities
        """
        heating_top_categories = ['Zentralheizung', 'Gas', 'Fernwärme']
        energy_top_categories = ['Gas', 'Fernwärme', 'Wärmepumpe']
        probabilities_heating = [0.7, 0.15, 0.15]  
        probabilities_energy = [0.6, 0.3, 0.1]  

        self.df.loc[self.df['heating'] == 'na', 'heating'] = np.random.choice(heating_top_categories, size=df_clean[df_clean['heating']=='na'].shape[0], p=probabilities_heating)
        self.df.loc[self.df['energy'] == 'na', 'energy'] = np.random.choice(energy_top_categories, size=df_clean[df_clean['energy']=='na'].shape[0], p=probabilities_energy)

    def prepare_features(self):
        """
        Select features and encode categorical variables
        """
        X = self.df[['area', 'rooms', 'heating', 'energy', 'zipcode']]
        X = pd.get_dummies(X, columns=['heating', 'energy', 'zipcode'], drop_first=True)

        y = self.df['price']

        return X, y
    
    def split_data(self, X, y):
        """
        Split dataset into train and test
        """
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        return X_train, X_test, y_train, y_test
    
    def scale_data(self, X_train, X_test):
        """
        Scale numeric features
        """
        scaler = StandardScaler()

        numeric_cols = ['area', 'rooms']

        X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
        X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])

        return X_train, X_test