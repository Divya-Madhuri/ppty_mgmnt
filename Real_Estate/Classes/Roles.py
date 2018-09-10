from Configs.app_config import db


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String, primary_key=True)
    People = db.relationship('People', backref='Roles', lazy=True)

    def __init__(self, role_id, name):
        self.id = role_id
        self.role = name


db.create_all()


