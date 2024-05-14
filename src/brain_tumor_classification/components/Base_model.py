from src.brain_tumor_classification.exception import Custom_Exception
from src.brain_tumor_classification.utils.common import *
from src.brain_tumor_classification.constants import *
from src.brain_tumor_classification.entity import *
from src.brain_tumor_classification.logger import logging 
import tensorflow as tf 
from tensorflow.keras.models import save_model
from tensorflow import keras 
from tensorflow.keras.models import Model 
from pathlib import Path
from tensorflow.keras.layers import Dense,GlobalMaxPooling2D,Flatten,Dropout
from tensorflow.keras.models import Model,Sequential
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from dataclasses import dataclass
from pathlib import Path
import os 
import sys 






class Prepare_base_model:
    
    def __init__(self,config1:Base_model):
        self.config=config1

    def prepare_base_model(self):
        self.base_mod=tf.keras.applications.vgg16.VGG16(input_shape=self.config.Image_size,include_top=self.config.include_top,weights=self.config.weights)


        save_model(filepath=self.config.model_weights,model=self.base_mod)

        return self.base_mod
    


    def prepare_full_model(self,model):
        for layer in model.layers:
            layer.trainable = False   ## it will preserve the initail weights of the model 

        x=model.output 
        x=tf.keras.layers.GlobalAveragePooling2D()(x)
        x=tf.keras.layers.Dense(256,activation="relu")(x)
        prediction=tf.keras.layers.Dense(4,activation="softmax")(x)

        full_model=Model(inputs=model.input,outputs=prediction)

        full_model.compile(optimizer=tf.keras.optimizers.Adam(),loss=tf.keras.losses.CategoricalCrossentropy(),metrics=["accuracy"])

        full_model.summary()

        save_model(filepath=self.config.updated_model_weights,model=full_model)

        return full_model 
    
    
    


