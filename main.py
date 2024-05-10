from src.brain_tumor_classification.pipeline import data_ingestion_pipeline
from src.brain_tumor_classification.logger import logging 
from src.brain_tumor_classification.exception import Custom_Exception
import sys


try:
    a=data_ingestion_pipeline()
    logging.info('data ingestion has been started')
    a.main()
    logging.info('data ingestion has been completed')
except Exception as e:
    raise(Custom_Exception(e,sys))


