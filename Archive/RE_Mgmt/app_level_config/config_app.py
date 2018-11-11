from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/divyamadhuri/Documents/Python/ppty_mgmnt/RE_Mgmt/REM_DB.db'


db = SQLAlchemy(app)
