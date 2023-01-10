from flask import ( Blueprint, render_template, request, redirect ) 
bp = Blueprint(
    'signup',
    __name__,
    url_prefix="/signup"
)

@bp.route('/')
def signup():
    return render_template('signup.html')


