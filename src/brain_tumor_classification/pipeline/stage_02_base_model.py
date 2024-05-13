from src.brain_tumor_classification.config import *
from src.brain_tumor_classification.exception import Custom_Exception
from src.brain_tumor_classification.components import Prepare_base_model
from pathlib import Path

class BASE_MODEL:

    def base_model(self):
            pass
    

    def main(self):
            try:
                config=Configuration_manager()
                config=config.base_model_config()
                a=Prepare_base_model(config1=config)
                a.prepare_base_model()
    
            except Exception as e:
                raise(Custom_Exception(e,sys))