from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////Users/divyamadhuri/Documents/Python/ppty_mgmnt/SQLAlchemy_work/sqlalchemyDB.db'
db = SQLAlchemy(app)


class Users(db.Model):
    user_id = db.Column('User_id', db.Integer, primary_key=True)
    user_name = db.Column('User_Name', db.String)
    age = db.Column('Age', db.Integer)
    address = db.Column('Address', db.String)

    def __init__(self, user_id, user_name, age, address=None):
        self.user_id = user_id
        self.user_name = user_name
        self.age = age
        self.address = address


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    insert_user1 = Users(6,'Srikanth', 33, 'H-No : 9-1-150 and etc')
    insert_user2 = Users(7,'Samanvisri', 1, 'H-No : 9-1-150 and etc')
    insert_user3 = Users(5,'Some random', 26, 'H-No : 9-1-150 and etc')

    db.session.add(insert_user1)
    db.session.add(insert_user2)
    db.session.add(insert_user3)
    db.session.commit()
    return 'data entered into table'


@app.route('/delete')
def delete():
    del_user1 = Users.query.filter_by(user_id=5).first()
    db.session.delete(del_user1)
    db.session.commit()
    return 'data deleted from table'


db.create_all()
app.run(debug=True)
