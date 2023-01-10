from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('login', __name__, url_prefix="/login")

@bp.route('/')
def login():
    return render_template('login.html')
