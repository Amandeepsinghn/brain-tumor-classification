import tensorflow as tf 
import os 
from tensorflow import keras 
from src.brain_tumor_classification.constants import *
from src.brain_tumor_classification.config import *
from src.brain_tumor_classification.entity import *
from src.brain_tumor_classification.logger import logging
from src.brain_tumor_classification.exception import Custom_Exception
from src.brain_tumor_classification.utils.common import *
import sys 
from datetime import datetime 









class Evaulation_start:
    try:
        def __init__(self,config:evaluation):
            self.config=config


        def train_images(self):
            self.train_ds=tf.keras.preprocessing.image.ImageDataGenerator(
                    rescale=1./255.,
                    validation_split=0.2,
                    horizontal_flip=True,rotation_range=0.2,zoom_range=0.2)
        
            self.val_ds=tf.keras.preprocessing.image.ImageDataGenerator(
                rescale=1./255.,
                validation_split=0.2
            )
        
            self.train_img=self.train_ds.flow_from_directory(self.config.training_data,target_size=(224,224),
                                                        class_mode="categorical",batch_size=12,seed=1337,
                                                        subset="training")
        
            self.valid_img=self.val_ds.flow_from_directory(self.config.training_data,target_size=(224,224),
                                                    class_mode="categorical",batch_size=12,seed=1337,
                                                    subset="validation")
        
    
        def load_model(self):
            return tf.keras.models.load_model(self.config.model_path)
    


        def evaluation(self):
            self.model=self.load_model()
        
            self.score=self.model.evaluate(self.valid_img)

    
        def evaluate_score(self):
            return f"loss is {self.score[0]} and accuracy is {self.score[1]}"
        

    except Exception as e:
        raise(Custom_Exception(e,sys))