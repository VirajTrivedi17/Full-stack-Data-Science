from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('d_tree_classifier.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Age = request.form['Age']
        Sex = request.form['Sex']
        Pclass = request.form['Pclass']
        Embarked = request.form['Embarked']
        Family = request.form['Family']
        Is_alone = request.form['Is_alone']

        try:    
            prediction = model.predict([[ Age, Sex, Pclass, Embarked, Family, Is_alone]])
        
            
            if prediction[0] == 1:
                return render_template('result.html',prediction_text="TRAVELLER SURVIVED 😃")
            else:
                return render_template('result.html',prediction_text="TRAVELLER DIED 😟😮")
            
            print(prediction[0])
            
        except:
            return render_template('index.html')
        
        
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

