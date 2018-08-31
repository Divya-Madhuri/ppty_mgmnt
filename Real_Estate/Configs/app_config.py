from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/divyamadhuri/Documents/Python/ppty_mgmnt/Real_Estate/RESdb.db'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)
