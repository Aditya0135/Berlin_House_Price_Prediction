from Berlin_House_Price_Prediction.constants import *
from Berlin_House_Price_Prediction.utils.common import read_yaml,create_directories
from Berlin_House_Price_Prediction.entity.config_entity import DataIngestionConfig
from Berlin_House_Price_Prediction.entity.config_entity import DataValidationConfig
from Berlin_House_Price_Prediction.entity.config_entity import DataTransformationConfig

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