# components 
from src.brain_tumor_classification.exception import Custom_Exception
from src.brain_tumor_classification.constants import *
from tensorflow.keras.layers import Dense,GlobalMaxPooling2D,Flatten,Dropout
from tensorflow.keras.models import Model,Sequential
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from dataclasses import dataclass
from pathlib import Path
from src.brain_tumor_classification.utils.common import *
from src.brain_tumor_classification.utils.common import *
from src.brain_tumor_classification.entity import *
import tensorflow as tf
from tensorflow.keras.models import save_model





class Prepare_base_model:
    
    def __init__(self,config1:Base_model):
        self.config=config1

    def prepare_base_model(self):
        self.base_mod=tf.keras.applications.vgg16.VGG16(input_shape=self.config.Image_size,include_top=self.config.include_top,weights=self.config.weights)

        self.base_mod.summary()

        save_model(filepath=self.config.model_weights,model=self.base_mod)
    


    def prepare_full_model(self,model):
        for i in model.layers:
            i.trainable=False   ## it will preserve the initail weights of the model 

        x=model.output 
        x=tf.keras.layers.GlobalAveragePooling2D()(x)
        x=tf.keras.layers.Dense(256,activation="relu")(x)
        prediction=tf.keras.layers.Dense(4,activation="softmax")

        model=Model(inputs=model.input,outputs=prediction)

        model.compile(optimizer=tf.keras.optimizers.Adam,loss=tf.keras.losses.CategoricalCrossentropy,metrics=["accuracy"])

        model.summary()

        save_model(filepath=self.config.updated_model_weights,model=model)

        return model 
    