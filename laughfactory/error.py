from flask import ( Blueprint, render_template, request, redirect ) 
bp = Blueprint(
    'error',
    __name__,
    url_prefix="/error"
)

@bp.route('/')
def signup():
    return render_template('error.html')