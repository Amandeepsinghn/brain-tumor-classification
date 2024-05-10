from pathlib import Path
from src.brain_tumor_classification.utils.common import *
from src.brain_tumor_classification.entity import *
from src.brain_tumor_classification.logger import logging 
from src.brain_tumor_classification.exception import Custom_Exception
import sys
from src.brain_tumor_classification.config import *
from src.brain_tumor_classification.components import *



class data_ingestion_pipeline:
    
    def __init__(self):
        pass

    def main(self):

        try:
            b=Configuration_manager()
            x=b.config_manager()
            v=comp_data_ingestion(x)
            v.extract_data()

        except Exception as e:
            raise(Custom_Exception(e,sys))