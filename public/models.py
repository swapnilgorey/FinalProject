from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(200),unique=True)
    username = db.Column(db.String(200), unique=True)
    firstName=db.Column(db.String(200))
    lastName=db.Column(db.String(200))
    password=db.Column(db.String(200))
    posts=db.relationship('Post')

class Post(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    postTitle = db.Column(db.String(1000))
    postData = db.Column(db.String(100000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    imgurl=db.Column(db.String(200))
    videourl = db.Column(db.String(200))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))