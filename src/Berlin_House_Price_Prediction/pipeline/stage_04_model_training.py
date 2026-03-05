from Berlin_House_Price_Prediction.config.configuration import ConfigurationManger
from Berlin_House_Price_Prediction.components.model_trainer import ModelTrainer
from Berlin_House_Price_Prediction import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        model_training_config = config.get_model_trainer_config()
        model_training = ModelTrainer(config=model_training_config)
        model_training.train()

if __name__ == "main":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    