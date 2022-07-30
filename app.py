# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  StandardScaler
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template
import re
import math
import pickle

app = Flask("__name__")

q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")



@app.route("/predict", methods=['POST'])
def predict():
    
    model = pickle.load(open("water_potability.sav", "rb"))
    

    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']

    
    
    
    
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7,
     inputQuery8, inputQuery9]]
    
    # Create the pandas DataFrame 
    new_df = pd.DataFrame(data, columns = ['Hardness', 'Solids', 'Chloramines','Conductivity',
    'Organic_carbon','Turbidity','Sulphates','Trihalomethanes','ph'])

    sc = StandardScaler()
    features = new_df.columns
    new_df[features] = sc.fit_transform(new_df[features])

    single = model.predict(new_df)
    if single==1:
        o1 = "The water is Potable"
    else:
        o1 = "The patient is not Potable"
    
    return render_template('home.html', output1=o1, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],
    query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7 = request.form['query7'],
    query8 = request.form['query8'],query9 = request.form['query9'])
    
if __name__ == "__main__":
    app.run(debug=True)