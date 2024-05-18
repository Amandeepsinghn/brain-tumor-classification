from src.brain_tumor_classification.pipeline import data_ingestion_pipeline
from src.brain_tumor_classification.logger import logging 
from src.brain_tumor_classification.exception import Custom_Exception
import sys
from src.brain_tumor_classification.pipeline import Model_pipeline
from src.brain_tumor_classification.pipeline import training_pipeline
from src.brain_tumor_classification.pipeline import evaluation_pipeline

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



try:
    c=training_pipeline()
    logging.info("model training has been started")
    c.main()
    logging.info("model training has been done")

except Exception as e:
    raise(Custom_Exception(e,sys))



try:
    d=evaluation_pipeline()
    logging.info('evaluation has started')
    d.main()
    logging.info("evaluation has been done")

except Exception as e:
    raise(Custom_Exception(e,sys))