from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from joblib import load

app = Flask(__name__)
model = load("model.joblib")

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':        
        age = request.form['age']
        gender = request.form['gender']
        race = request.form['race']
        edu_num = request.form['edu_num']
        workclass = request.form['workclass']
        marital_status = request.form['marital_status']
        relationship = request.form['relationship']
        hours_per_week = request.form['hours_per_week']
        capital_gain = request.form['capital_gain']
        capital_loss = request.form['capital_loss']        
        fnlwgt = request.form['fnlwgt']

        print("Data Received from HTML Successfully")

        try:    
            print("Entered the TRY Block")
            print("Trying to Predict............")            
            d = [[age, gender, race, edu_num, workclass, marital_status, relationship, hours_per_week, capital_gain, capital_loss, fnlwgt]]
#            data = np.array(d).reshape(1,-1) 
            
            result = model.predict(d)[0]
            print("PREDICTION DONE")
            
            if result == 1:
                print("try - if block entered")
                return render_template('result.html', prediction_text = "INCOME GREATER THAN $50K 😃")
            else:
                return render_template('result.html', prediction_text = "INCOME LESSER THAN $50K 😟😮")
            
            print(prediction[0])
            
        except Exception as e:
            print("Entered Except Block")
            print(f"Exception: {e}")
            return render_template('index.html')
        
        
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

