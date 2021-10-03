
# Boston House Price Prediction

**Demo: https://boston-houseprice-prediction04.herokuapp.com/**

### PROJECT DESCRIPTION
The context of this project is to predict the prices of the Houses of Boston, Massachusetts
using Linear Regression Machine Learning algorithm that played an important role in predicting 
the prices of the houses using various independent features.

### AIM & OBJECTIVE
The aim of this project is to investigate the Linear Regression Algorithm executed in various areas and evaluate the performance of the chosen machine learning
algorithms to find out the best suitable and efficient model for the chosen data set.

#### OBJECTIVE
- To understand the efficient machine learning technique for predicting the prices.
- To evaluate the performance of the selected machine learning algorithm.

### ABOUT THE DATA
    Number of Instances: 506 

    Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.

    Attribute Information (in order):
        - CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000's

    Missing Attribute Values: None

    Creator: Harrison, D. and Rubinfeld, D.L.

    This is a copy of UCI ML housing dataset.
    https://archive.ics.uci.edu/ml/machine-learning-databases/housing/


### TECHNICAL ASPECTS

#### DATA PREPROCESSING
- Checked for Null Values 
- Aggregating the Boston Features with the Target Attribute

#### STATISTICAL ANALYSIS OF DATA
- Description of the data
    ```
    Data.describe()
    ```
- Finding the correlation
    ```
    Data.corr()
    ```
- Correlation Matrix with Heatmap
    ```
    mask1 = np.zeros_like(Data.corr()) 
    # This will create a table of 0 similar to the size of Data.corr()
    
    triangle_indices= np.triu_indices_from(mask1)
    
    mask1[triangle_indices] = True 
    # This will make the top triangle values true
    
    mask1

    ```

![App Screenshot](https://github.com/khwajaavais/Boston-House-Price-Prediction/blob/8a3aeeab68c3fc71b966a1d38481ebb41815f56a/Correlation.png)

#### FEATURE SELECTION
You can get the feature importance of each feature of your dataset by using the feature importance property of the model.

Feature importance gives you a score for each feature of your data, the higher the score more important or relevant is the feature towards your output variable.

Feature importance is an inbuilt class that comes with Tree Based Regressor, we will be using Extra Tree Regressor for extracting the top 10 features for the dataset.

Some of the least important features like **INDUS, TAX, B** weren`t included in the actual predicted model.


#### IMPLEMENTATION OF LINEAR MODEL
The implementation of Boston House Price Prediction is done in 2 ways:

1. The Linear Regression Implementation (with all attributes)

        The matrix evaluation for this model       
     
            RSquared Value: 0.6793145308022446
            MSE Value:      33.537524632703274
            RMSE Value:     5.791159178670819
            MAE Value:      4.082624372810914


2. The Linear Regression Implementation with Recursive Feature Elimination (RFE) 

Using RFE some of the least important features like INDUS, TAX, B weren`t included in the actual predicted model.

        The matrix evaluation for this model

            RSquared Value: 0.6793145308022446
            MSE Value:      33.537524632703274
            RMSE Value:     5.791159178670819
            MAE Value:      4.082624372810914


**There weren`t much different between both these models for used the second model for prediction**

### MODEL DEPLOYMENT: 

**LOCALHOST**

For implementating the project in your own system follow the steps;
- Download the directory
- Open the Command Prompt (CLI) and change the path to this file path
- Run the command
```
    python app.py
```
- Hit http://127.0.0.1:5000/


**WEB APPLICATION**

For deploying the project via Heroku platform 

Follow Krish Naik`s **Deployment of ML models in Heroku using Flask**  
https://www.youtube.com/watch?v=mrExsjcvF4o


**Note:** Mandatory Files required while deploying ML Model in Heroku using Flask
    
1. app.py  
2. Procfile
3. .pkl file (Pickle File)
4. request.py 
5. requirement.txt
6. templates / index.html (UI File)
7. static/css/ style.css 

(You can use my Repository to follow the steps)



### INSTALLATION
The Code is written in Python 3.7. If you don't have Python installed you can find it [there](https://www.python.org/downloads/)
. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 
To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

    pip install -r requirements.

### CONCLUSION
- Implementation of Linear Regression Algorithm for the House Price prediction is successful. 

- The model can predict the prices for the houses entered by the end user.
- Implementation of Linear Regression can be done in all the Supervised Learning Data.
## Screenshots

**Demo: https://boston-houseprice-prediction04.herokuapp.com/**


**INDEX PAGE**

![App Screenshot](https://github.com/khwajaavais/Boston-House-Price-Prediction/blob/ab2077afb5ee1206e1c8a1d21d4aa20d84543f78/templates/127.0.0.1_5000_(screenshot).png)


**RESULT PAGE**

![App Screenshot](https://github.com/khwajaavais/Boston-House-Price-Prediction/blob/ab2077afb5ee1206e1c8a1d21d4aa20d84543f78/templates/127.0.0.1_5000_predict(screenshot).png)