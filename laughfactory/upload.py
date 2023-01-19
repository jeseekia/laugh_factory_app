from flask import ( Blueprint, render_template, request, redirect ) 
bp = Blueprint(
    'upload',
    __name__,
    url_prefix="/upload"
)

@bp.route('/')
def upload():
    return render_template('upload.html', upload="upload.html")
