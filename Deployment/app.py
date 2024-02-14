from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import json
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
Bootstrap(app)
# Load model and data files during application startup
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading the model:", e)
    model = None
with open('output.json', 'r') as f:
    data = json.load(f)
with open('age_map.json', 'r') as f1:
    age_map = json.load(f1)
# Preload column names
column_names = (
    'Age_Scaled', 'Sex', 'A0', 'A1', 'A4', 'A5', 'A8', 'A9', 'B3', 'B4',
    'B5', 'B9', 'C0', 'C4', 'C5', 'C6', 'C7', 'C8', 'D0', 'D1', 'D2', 'D3',
    'D4', 'D5', 'E0', 'E1', 'E2', 'E5', 'E7', 'E8', 'F1', 'F2', 'G0', 'G2',
    'G3', 'G8', 'H0', 'H6', 'I0', 'I1', 'I8', 'I9', 'J0', 'J3', 'K0', 'K2',
    'K4', 'K5', 'K7', 'K9', 'L0', 'M0', 'M3', 'M4', 'M6', 'M7', 'M8', 'N1',
    'N4', 'N6', 'O0', 'O6', 'P0', 'Q0', 'R0', 'R1', 'R7', 'S0', 'S2', 'S3',
    'T1', 'U0', 'Z0', 'Z3', 'Z4', 'Z9'
)
@app.route('/')
def index():
    return render_template('website.html')
@app.route('/predict', methods=['POST'])
def predict_placement():
    age = request.form.get('Age')
    sex = request.form.get('Sex')
    diag = request.form.get('DiagnosisType')
    sex_value = 0 if sex == 'M' else 1
    diagnosis_bs = data.get(diag, [])
    age_value = age_map.get(age, 38)
    X_pred = [age_value, sex_value] + diagnosis_bs
    X_pred_df = pd.DataFrame([X_pred], columns=column_names)
    prediction = model.predict(X_pred_df)
    result = 'Approved' if prediction[0] == 'Paid' else 'Denied'
    return render_template('website.html', result=result)
@app.route('/diagnosis-page.html')
def diagnosis_page():
    return render_template('next_page.html')
if __name__ == '__main__':
    app.run()





