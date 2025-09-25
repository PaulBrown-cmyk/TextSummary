from src.TextSummary.logging import logger
from src.TextSummary.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummary.pipeline.stage2_data_transformation import DataTransformationTrainingPipeline

STAGE_INGESTION = 'Data Ingestion Stage'
STAGE_TRANSFORMATION = 'Data Transformation Stage'

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
    logger.info('\u2705  -  DONE')
    logger.close()
except Exception as E:
    logger.exception(E)
    raise E
