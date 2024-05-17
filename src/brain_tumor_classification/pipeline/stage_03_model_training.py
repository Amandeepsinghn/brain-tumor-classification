from src.brain_tumor_classification.exception import Custom_Exception
import sys 
from src.brain_tumor_classification.config import *
from src.brain_tumor_classification.components import *





class training_pipeline:
    def __init__(self):
        pass 

    def main(self):
        try:
            a=Configuration_manager()
            v=a.config_check()
            z=a.training_config()
            chk=comp_checkpoint_ingestion(v)
            t=chk.callback_tb_ckt()
            c=chk.create_chkpt_callbacks()
            tc=chk.callback_tb_ckt()
            T=Training(z)
            T.get_updated_base_model()
            T.train_images()
            T.train_model(tc)

        except Exception as e:
            raise(Custom_Exception(e,sys))