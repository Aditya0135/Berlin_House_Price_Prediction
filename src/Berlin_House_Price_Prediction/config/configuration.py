from Berlin_House_Price_Prediction.constants import *
from Berlin_House_Price_Prediction.utils.common import read_yaml,create_directories
from Berlin_House_Price_Prediction.entity.config_entity import DataIngestionConfig,DataTransformationConfig,DataValidationConfig,ModelTrainerConfig,ModelEvaluationConfig

# this class has a constructor which reads the yaml files
class ConfigurationManger:
    # Reading yaml file and create root directory
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH
                 ):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        create_directories([self.config.artifacts_root])


    # 
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_directory])

        data_ingestion_config = DataIngestionConfig(
            root_directory=config.root_directory,
            source_url=config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        
        return data_ingestion_config
    

    def get_data_validation_config(self)->DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_directory])

        data_validation_config = DataValidationConfig(
            root_directory= config.root_directory,
            unzip_data_dir= config.unzip_data_dir,
            STATUS_FILE = config.STATUS_FILE,
            all_schema= schema,
        )

        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_directory])

        data_transformation_config = DataTransformationConfig(
            root_directory= config.root_directory,
            data_path= config.data_path,
            test_size= config.test_size,
            random_state= config.random_state,
            features= config.features,
            target= config.target,
            numeric_features= config.numeric_features,
            categorical_features= config.categorical_features
        )

        return data_transformation_config
    
    def get_model_trainer_config(self)->ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.GradientBoostingRegressor

        create_directories([config.root_directory])

        model_trainer_config = ModelTrainerConfig(
            root_directory= config.root_directory,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            n_estimators= params.n_estimators,
            learning_rate= params.learning_rate,
            random_state= params.random_state,
            target_column= self.schema.TARGET_COLUMN
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.GradientBoostingRegressor
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_directory])

        model_evaluation_config = ModelEvaluationConfig(
            root_directory= config.root_directory,
            test_data_path= config.test_data_path,
            model_path= config.model_path,
            all_params= params,
            metric_file_name= config.metric_file_name,
            target_column= schema.name,
            mlflow_uri= "https://dagshub.com/Aditya0135/Berlin_House_Price_Prediction.mlflow",
        )

        return model_evaluation_config
    
    