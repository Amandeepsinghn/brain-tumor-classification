import tensorflow as tf 
from tensorflow.keras.models import load_model
import numpy as np 
from tensorflow.keras.preprocessing import image
import os



class cancer_classification:
    def __init__(self,filename):
        self.filename=filename 


    def prediction(self):
        #loading model 

        model=load_model(os.path.join("artifacts/base_model/model.VGG16.h5"))

        imagename=self.filename

        test_image=image.load_img(imagename,target_size=(224,224))

        test_image=image.img_to_array(test_image)

        test_image=np.expand_dims(test_image,axis=0)

        result=np.argmax(model.predict(test_image),axis=1)

        print(result)

        
        if result[0]==1:
            prediction="glioma"
            return [{"image":prediction}]
        
        elif result[0]==2:
            prediction="meningioma"
            return [{'image':prediction}]
        
        elif result[0]==3:
            prediction="notumor"
            return [{'image':prediction}]
        
        else:
            prediction="pituitary"
            return [{'image':prediction}]
        

        


