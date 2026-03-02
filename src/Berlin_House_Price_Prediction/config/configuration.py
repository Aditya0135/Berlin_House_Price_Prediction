from Berlin_House_Price_Prediction.constants import *
from Berlin_House_Price_Prediction.utils.common import read_yaml,create_directories
from Berlin_House_Price_Prediction.entity.config_entity import DataIngestionConfig


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