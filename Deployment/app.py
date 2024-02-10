#importing dependencies
from flask import Flask,render_template, request, jsonify
from flask_bootstrap import Bootstrap
import json
import pickle
import numpy as np
import re
import pandas as pd 

#importing pickle file
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading the model:", e)
    model = None

#imporing one hot encoding json file
with open('output.json', 'r') as f:
    data = json.load(f)

#import age mapping json file
with open('age_map.json', 'r') as f1:
    age_map = json.load(f1)

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  @app.route('/')
  def index(): 
      return render_template('website.html')
  
  @app.route('/predict', methods=['Post'])
  def predict_placement():
      age = str(request.form.get('Age'))
      sex = str(request.form.get('Sex'))
      diag = str(request.form.get('DiagnosisType'))
      #retrieveing sex binary code 0 is male and 1 is female
      sex_value = None 
      if (sex == 'M'):
          sex_value = 0
      elif (sex == 'F'):
          sex_value = 1
      #Retriveing diagnosis bianary sequence 
      diagnosis = data[diag]
      #Determining scaled value of age
      age_value = age_map['38']
      extracted_numbers = re.findall(r'\d+', str(diagnosis))
      #Extracted binary sequence
      diagnosis_bs = list(map(int, extracted_numbers))
      #Pre loading dataframe colum nnames 
      column_names = ['Age_Scaled', 'Sex', 'A0', 'A1', 'A4', 'A5', 'A8', 'A9', 'B3', 'B4',
       'B5', 'B9', 'C0', 'C4', 'C5', 'C6', 'C7', 'C8', 'D0', 'D1', 'D2', 'D3',
       'D4', 'D5', 'E0', 'E1', 'E2', 'E5', 'E7', 'E8', 'F1', 'F2', 'G0', 'G2',
       'G3', 'G8', 'H0', 'H6', 'I0', 'I1', 'I8', 'I9', 'J0', 'J3', 'K0', 'K2',
       'K4', 'K5', 'K7', 'K9', 'L0', 'M0', 'M3', 'M4', 'M6', 'M7', 'M8', 'N1',
       'N4', 'N6', 'O0', 'O6', 'P0', 'Q0', 'R0', 'R1', 'R7', 'S0', 'S2', 'S3',
       'T1', 'U0', 'Z0', 'Z3', 'Z4', 'Z9']
      #Loading Values 
      X_pred = [age_value,sex_value]
      X_pred.extend(diagnosis_bs)
      #Loading everything into a dataframe
      X_pred_df = pd.DataFrame([X_pred], columns=column_names)
      #predciting Result using the values in dtaframe 
      prediction = model.predict(X_pred_df)
      predict = prediction[0]

      return str(predict)


  
  @app.route('/diagnosis-page.html')
  def diagnosis_page():
        return render_template('next_page.html')
  

  if __name__ == '__main__':
    app.run(debug=True)

  return app

create_app()


