from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////Users/divyamadhuri/Documents/Python/ppty_mgmnt/SQLAlchemy_work/sqlalchemyDB.db'
