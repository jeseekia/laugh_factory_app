# config
from flask import Flask
app = Flask(__name__)

# index route
@app.route('/')
def index():
    return 'Welcome to the LaughFactory'

# meme index route
@app.route('/memes')
def memes():
    return 'These are the memes'