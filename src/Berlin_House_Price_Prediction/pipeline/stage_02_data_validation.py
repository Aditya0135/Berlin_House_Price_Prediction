from Berlin_House_Price_Prediction.config.configuration import ConfigurationManger
from Berlin_House_Price_Prediction.components.data_validation import DataValidation
from Berlin_House_Price_Prediction import logger

STAGE_NAME = "Data Validation Stage"

class DataIngestionValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "main":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataIngestionValidationPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    