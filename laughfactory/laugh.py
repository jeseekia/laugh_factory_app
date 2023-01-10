from flask import ( Blueprint, render_template )
import json
bp = Blueprint(
    'meme',
    __name__,
    url_prefix="/memes"
)

@bp.route('/')
def index():
    return render_template('index.html',memes=memes)

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/signup')
def signup():
    return render_template('signup.html')

memes = json.load(open('meme.json'))