from Berlin_House_Price_Prediction import logger
from Berlin_House_Price_Prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Berlin_House_Price_Prediction.pipeline.stage_02_data_validation import DataIngestionValidationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataIngestionValidationPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e