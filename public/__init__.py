from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db=SQLAlchemy()
databaseName='database.db'


def createApp():
    app = Flask(__name__)
    app.secret_key="asdfgh"
    app.config['SECRET KEY'] = "MyFinalProject"
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{databaseName}'
    db.init_app(app)

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

