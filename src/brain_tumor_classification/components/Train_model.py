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
import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf






class Training:
    def __init__(self,config:Training_Config):
        self.config=config

    
    def get_updated_base_model(self):
        self.model=tf.keras.models.load_model(self.config.updated_model_weights)


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
        

    def train_model(self,callbacks_list:list):
        self.callbacks=callbacks_list
        self.model.fit(self.train_img,
                       epochs=self.config.params_epochs,
                       validation_data=self.valid_img,
                       callbacks=self.callbacks)
        
        self.model.save(self.config.trained_model_path)

