from src.TextSummary.logging import logger
from src.TextSummary.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummary.pipeline.stage2_data_transformation import DataTransformationTrainingPipeline
from src.TextSummary.pipeline.stage3_model_trainer import ModelTrainerPipeline
from src.TextSummary.pipeline.stage4_model_evaluation import ModelEvaluationPipeline

STAGE_INGESTION = 'Data Ingestion Stage'
STAGE_TRANSFORMATION = 'Data Transformation Stage'
STAGE_TRAINER = 'Model Trainer Stage'
STAGE_EVAL = 'Model Evaluation Stage'

logger.info('\u2705  -  START')
try:
    logger.info(f'Stage {STAGE_INGESTION} initiated.')
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f'Stage {STAGE_INGESTION} completed')
    logger.info(f'Stage {STAGE_TRANSFORMATION} initiated.')
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f'Stage {STAGE_TRANSFORMATION} completed.')
    logger.info(f'Stage {STAGE_TRAINER} initiated.')
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f'Stage {STAGE_TRAINER} completed.')
    logger.info(f'Stage {STAGE_EVAL} initiated.')
    model_evauation_pipeline = ModelEvaluationPipeline()
    model_evauation_pipeline.initiate_model_evaluation() 
    logger.info(f'Stage {STAGE_EVAL} completed.')
    logger.info('\u2705  -  DONE')
except Exception as E:
    logger.exception(E)
    raise E
