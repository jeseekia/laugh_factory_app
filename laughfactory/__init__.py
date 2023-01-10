from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return "Hello, it's Meme!"

    from . import index
    app.register_blueprint(index.bp)
    from . import login
    app.register_blueprint(login.bp)
    from . import signup
    app.register_blueprint(signup.bp)
    from . import upload
    app.register_blueprint(upload.bp)
    return app