from Configs.app_config import db
from Classes.Roles import Roles


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=True)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    mobile_num = db.Column(db.Integer)
    alternate_num = db.Column(db.Integer)
    address = db.Column(db.String)

    def __init__(self, pid, cust_name, role, gender, age, mobile_num, alternate_num, address):
            self.id = pid
            self.name = cust_name
            self.role = role
            self.gender = gender
            self.age = age
            self.mobile_num = mobile_num
            self.alternate_num = alternate_num
            self.address = address


db.create_all()




