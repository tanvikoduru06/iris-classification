# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 21:05:11 2021

@author: tanvv
"""

from flask import Flask, render_template, request
from flask_cors import cross_origin
#import jsonify
#import requests
import pickle
import numpy as np
#import sklearn
#from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('dt_model.pkl', 'rb'))
#model = pickle.load(r"C:\Users\tanvv\OneDrive\Documents\practice projects\dt_model.pkl", "rb")
@app.route('/',methods=['GET'])
@cross_origin()
def Home():
    return render_template('index.html')

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])
        y_pred = [[sepal_length,sepal_width,petal_length,petal_width]]
        model = pickle.load(open('dt_model.pkl', 'rb'))
        prediction=model.predict(y_pred)
        categories = ['iris-setosa','iris-versicolor','iris-virginica']
        prediction = categories[prediction[0]]
        return render_template('index.html',prediction_text="The type of Iris flower is : {}".format(prediction))
    return render_template("index.html")
    
     
    
        
    


if __name__=="__main__":
    app.run(debug=True)