#importing dependencies
from flask import Flask,render_template
from flask_bootstrap import Bootstrap



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


