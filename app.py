from flask import Flask,request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app = Flask(__name__)#Name of the application

#Route to home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')#This page contain a form for users to enter data.
    
    else:
        data=CustomData(
            step=int(request.form.get('step')),
            customer=request.form.get('customer'),
            age=request.form.get('age'),
            gender=request.form.get('gender'),
            zipcodeOri=request.form.get('zipcodeOri'),
            merchant=request.form.get('merchant'),
            zipMerchant=request.form.get('zipMerchant'),
            category=request.form.get('category'),
            amount=float(request.form.get('amount'))
        )
        pred_df = data.get_data_as_data_frame()#In predict_pipeline.py
        #print(pred_df)

        predict_pipeline = PredictPipeline()#Instantiating the class
        results = predict_pipeline.predict(pred_df)#Calling the predict function in PredictPipeline class
        if(results[0]==1):
            output="Fraudulent"
        else:
            output="Normal"
        return render_template('home.html',results=output)
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)