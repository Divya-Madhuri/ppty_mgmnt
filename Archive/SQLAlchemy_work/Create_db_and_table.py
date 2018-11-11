from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////Users/divyamadhuri/Documents/Python/ppty_mgmnt/SQLAlchemy_work/sqlalchemyDB.db'
db = SQLAlchemy(app)


class Family(db.Model):
    id = db.Column('personid', db.Integer, primary_key=True)
    name = db.Column('personname', db.String)
    age = db.Column('age', db.Integer)

    def __init__(self,pid , name, age):
        self.pid = pid
        self.name = name
        self.age = age
    print('data inserted successfully')


db.create_all()

