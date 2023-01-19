from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('index', __name__, url_prefix="/index")

@bp.route('/')
def index():
    return render_template('home.html')
