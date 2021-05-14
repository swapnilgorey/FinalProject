from flask import Flask
from .view import pages
from .auth import auth


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('/Users/swapnilgorey/Downloads/escribblethoughts-firebase-adminsdk-m5nce-505bca4dc4.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def createApp():
    app = Flask(__name__)
    app.secret_key="asdfgh"
    app.config['SECRET KEY'] = "MyFinalProject"



    app.register_blueprint(pages,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app