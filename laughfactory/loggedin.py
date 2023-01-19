from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('loggedin', __name__, url_prefix="/name")

@bp.route('/')
def loginned():
    return render_template('loggedin.html', loggedin="loggedin.html")
