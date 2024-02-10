#importing dependencies
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
import json
import pickle

try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading the model:", e)
    model = None

with open('output.json', 'r') as f:
    data = json.load(f)

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  @app.route('/')
  def index(): 
        return render_template('website.html')
  
  @app.route('/diagnosis-page.html')
  def diagnosis_page():
        return render_template('next_page.html')
  

  if __name__ == '__main__':
    app.run(debug=True)

  return app

create_app()


