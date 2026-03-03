from Berlin_House_Price_Prediction.config.configuration import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status=None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = data.columns
            all_schema_columns = self.config.all_schema.keys()


            for column in all_columns: 
                if column not in all_schema_columns:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                if data[column].dtype != self.config.all_schema[column]:
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Data type mismatch for column:{column} \nexpected: {self.config.all_schema[column]}\n received:{data[column].dtype}")
                
                
            return validation_status

        except Exception as e:
            raise e