
from flask_sqlalchemy import SQLAlchemy
from app_config import app

db = SQLAlchemy(app)


class Users2(db.Model):
    id = db.Column('User_id', db.Integer, primary_key=True)
    user_name = db.Column('User_Name', db.String)
    age = db.Column('Age', db.Integer)
    address = db.Column('Address', db.String)

    def __init__(self, user_id, user_name, age, address=None):
        self.user_id = user_id
        self.user_name = user_name
        self.age = age
        self.address = address


db.create_all()
