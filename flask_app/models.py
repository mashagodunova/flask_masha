from flask_app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

class Anketa(db.Model):
    __tablename__ = "anketa"
    id = db.Column(db.Integer, primary_key=True)
    quest1 = db.Column(db.String(200))
    quest2 = db.Column(db.String(200))
    quest3 = db.Column(db.String(200))
    quest4 = db.Column(db.String(200))
    quest5 = db.Column(db.String(200))
    quest6 = db.Column(db.String(200))
    comment = db.Column(db.String(1000))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(120))
    activity = db.Column(db.String(200))
    city = db.Column(db.String(200))

#    def __repr__(self):
#        return f'<Anketa from "{self.username}"/"{self.email}">'