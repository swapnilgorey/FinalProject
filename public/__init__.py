from flask import Flask
<<<<<<< HEAD
from .view import pages
from .auth import auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask_login import LoginManager
from .models import User
GOOGLE_APPLICATION_CREDENTIALS="/Users/swapnilgorey/Downloads/escribblethoughts-firebase-adminsdk-m5nce-505bca4dc4.json"

cred = credentials.Certificate('/Users/swapnilgorey/Downloads/escribblethoughts-firebase-adminsdk-m5nce-505bca4dc4.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
=======
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db=SQLAlchemy()
databaseName='database.db'
>>>>>>> origin/master

def createApp():
    app = Flask(__name__)
    app.secret_key="asdfgh"
    app.config['SECRET KEY'] = "MyFinalProject"
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{databaseName}'
    db.init_app(app)

<<<<<<< HEAD
    app.register_blueprint(pages,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return id
    return app
=======
    from .view import pages
    from .auth import auth

    app.register_blueprint(pages,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . models import User
    createDB(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)
    return app

def createDB(app):
    if not path.exists ('public/'+databaseName):
        db.create_all(app=app)
        print("created database successfully!!")
>>>>>>> origin/master
