from src.brain_tumor_classification.pipeline import data_ingestion_pipeline
from src.brain_tumor_classification.logger import logging 
from src.brain_tumor_classification.exception import Custom_Exception
import sys
from src.brain_tumor_classification.pipeline import Model_pipeline

try:
    a=data_ingestion_pipeline()
    logging.info('data ingestion has been started')
    a.main()
    logging.info('data ingestion has been completed')

except Exception as e:
    raise(Custom_Exception(e,sys))


try:
    b=Model_pipeline()
    logging.info("preparing base model")
    b.main()
    logging.info("base model has been made")

except Exception as e:
    raise(Custom_Exception(e,sys))


