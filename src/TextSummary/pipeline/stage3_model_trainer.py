from src.TextSummary.config.configuration import ConfigurationManager
from src.TextSummary.components.model_trainer import ModelTrainer
from src.TextSummary.logging import logger

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass
    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

