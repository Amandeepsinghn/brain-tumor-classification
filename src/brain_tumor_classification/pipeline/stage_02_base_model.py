from src.brain_tumor_classification.exception import Custom_Exception
import sys 
from src.brain_tumor_classification.config import *
from src.brain_tumor_classification.components import *






class Model_pipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=Configuration_manager()
            config=config.base_model_config()
            a=Prepare_base_model(config1=config)
            b=a.prepare_base_model()
            a.prepare_full_model(model=b)
    
        except Exception as e:
            raise(Custom_Exception(e,sys))