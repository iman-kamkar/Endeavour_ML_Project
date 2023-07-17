from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
            X_str = request.form.get('X')
            if X_str is not None:
                X = float(X_str)

            predict_pipeline=PredictPipeline()
            results=predict_pipeline.predict(X)
            
            return render_template('home.html', results=results[0][0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)        