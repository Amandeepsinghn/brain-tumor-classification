from flask import Flask,render_template,request,jsonify
import os 
from src.brain_tumor_classification.pipeline import cancer_classification
from src.brain_tumor_classification.utils.common import *




app=Flask(__name__)

class ClientApp:
    def __init__(self):
        self.filename="inputImage.jpg"
        self.classifier=cancer_classification(self.filename)


@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")







@app.route("/predict",methods=["POST"])
def predictRoute():
    image=request.json["image"]
    decodeImage(image,clapp.filename)

    result=clapp.classifier.prediction()

    return jsonify(result)




if __name__=="__main__":
    clapp=ClientApp()
    app.run(host="0.0.0.0",port=8080)

