# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Table, Column, MetaData, bindparam

from flask import Flask, jsonify
from flask_cors import CORS

username = 'postgres'
password = 'myproject'
hostname = 'database-1.cfg4ma0mq56c.us-east-2.rds.amazonaws.com'
port = '5432'
database_name = 'tx-dx'
# for creating connection engine
engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database_name}')


#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#Runs all route to CORS allow cross origin sharing
CORS(app)

#################################################
# Flask Routes
#################################################

#Route to Welcome page 
@app.route("/")
def welcome():
    """ Welcome to the Tx 2 Dx APP"""
    return (
        f"Welcome to the Tx 2 Dx Page!"
    )