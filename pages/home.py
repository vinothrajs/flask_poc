# pages/home.py

from flask import redirect, render_template, Blueprint, url_for

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('home.html')
