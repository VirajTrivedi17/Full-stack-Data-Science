from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('linear_reg.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/model_predict", methods=['POST'])
def model_predict():
    
    if request.method == 'POST':
        crime = request.form['crime']
        zone = request.form['zone']        
        charles_river = request.form['charles_river']
        NOX = request.form['NOX']
        average_rooms = request.form['average_rooms']
        age = request.form['age']
        distance = request.form['distance']
        accessible_highways = request.form['accessible_highways']
        student_teacher_ratio = request.form['student_teacher_ratio']
        LSTAT = request.form['LSTAT'] 

        try:    
            prediction = model.predict([[ crime, zone, charles_river, NOX,
                                            average_rooms, age, distance, accessible_highways, student_teacher_ratio, LSTAT]])
        
            return render_template('result.html',prediction_text="PREDICTED HOUSE PRICE : ${}".format(round(prediction[0] * 1000 ,2)))
            
            print(prediction[0])
            
        except:
            return render_template('index.html')
        
        
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

