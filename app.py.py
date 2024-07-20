from flask import Flask,render_template,request
import os
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)

encoders_path=os.path.dirname(os.path.abspath(__file__))
#model=pickle.load(open('insurance_detection.pkl','rb'))

#model=pickle.load(open('insurance_detection.pkl','rb'))
def load_pickle():
    with open('insurance_detection.pkl', 'rb') as f:
        loaded_pickle = pickle.load(f)
        return loaded_pickle
    

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/prediction',methods=['POST','GET'])
def predict():
    print(request.method)
    if request.method=='POST':
        #months_as_customer=float(request.form['months_as_customer'])
        age=float(request.form['age'])
        policy_number=float(request.form['policy_number'])
        umbrella_limit=float(request.form['umbrella_limit'])
        
        policy_annual_premium=float(request.form['policy_annual_premium'])
        insured_zip=float(request.form['insured_zip'])
        capital_gain=float(request.form['capital_gain'])
        incident_hour_of_the_day=float(request.form["incident_hour_of_the_day"])
        number_of_vehicles_involved=float(request.form["number_of_vehicles_involved"])
        injury_claim=float(request.form['injury_claim'])
        bodily_injuries=float(request.form["bodily_injuries"])
        vechile_claim=float(request.form['total_claim_amount'])
        auto_year=float(request.form['auto_year'])

        pred =[[age,policy_number,umbrella_limit,policy_annual_premium,insured_zip,capital_gain,incident_hour_of_the_day,
                number_of_vehicles_involved,injury_claim,bodily_injuries,auto_year,vechile_claim]]
        #prediction=load_pickle.predict(pred)
        

        result="Legal Insurance Claim" if pred==1 else "Fraud Insurance Claim"
        return render_template('result.html',prediction_text=result)
        #print(result)
    return render_template("prediction.html")

if __name__=='__main__':
    app.run(debug=True)