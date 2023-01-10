from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('meme', __name__, url_prefix="/meme")

