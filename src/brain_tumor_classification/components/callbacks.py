from src.brain_tumor_classification.exception import Custom_Exception
from src.brain_tumor_classification.config import *
from datetime import datetime
import tensorflow as tf
from tensorflow import keras 
import os 
from src.brain_tumor_classification.entity import *
from src.brain_tumor_classification.logger import logging
from src.brain_tumor_classification.utils.common import *
from src.brain_tumor_classification.constants import *



# components
class comp_checkpoint_ingestion:
    def __init__(self,config1:check_):
        self.config=config1


    def create_tb_intialization(self):

        a=datetime.now().strftime("%H-%M")

        running_logs=os.path.join(self.config.tensorboard_dir,a)

        return tf.keras.callbacks.TensorBoard(log_dir=running_logs)

    
    def create_chkpt_callbacks(self):

        a=datetime.now().strftime("%s")[8:]

        model_path=os.path.join(self.config.checkpoint,f"model{str(a)}.h5")

        return tf.keras.callbacks.ModelCheckpoint(filepath=model_path,save_best_only=True)

        
    

    def callback_tb_ckt(self):
        
        return [self.create_tb_intialization(),self.create_chkpt_callbacks()]