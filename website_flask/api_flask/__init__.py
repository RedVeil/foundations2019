import os

from flask import Flask, render_template  

def create_app():
    # create and configure the app
    app = Flask(__name__,)
    app.config['SECRET_KEY'] = 'test'


    @app.route('/hello')
    def hello():
        return render_template("index.html")

    from . import dogs
    app.register_blueprint(dogs.bp)


    return app