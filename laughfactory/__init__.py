from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:tyler7820@localhost:5432/laugh-factory-app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)

    @app.route('/')
    def hello():
        return "Hello, it's Meme!"

    from . import meme
    app.register_blueprint(meme.bp)
    return app