from src.brain_tumor_classification.exception import Custom_Exception
import sys 
from src.brain_tumor_classification.config import *
from src.brain_tumor_classification.components import *



class evaluation_pipeline:
    def __init__(self):
        pass 

    def main(self):
        try:
            a=Configuration_manager()
            eval_=a.evluation_config()
            z=Evaulation_start(eval_)
            z.train_images()
            z.evaluation()
            z.evaluate_score()


        except Exception as e:
            raise Custom_Exception(e,sys)
