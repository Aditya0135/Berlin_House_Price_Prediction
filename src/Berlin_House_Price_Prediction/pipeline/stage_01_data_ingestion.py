from Berlin_House_Price_Prediction.config.configuration import ConfigurationManger
from Berlin_House_Price_Prediction.components.data_ingestion import DataIngestion
from Berlin_House_Price_Prediction import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()

if __name__ == "main":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    