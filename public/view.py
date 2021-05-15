from flask import Blueprint, render_template
from flask_login import login_required,current_user
pages = Blueprint('pages',__name__)

@pages.route('/')
@login_required
def home():
    return render_template("home.html")
