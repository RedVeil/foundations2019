import os

from flask import Flask, render_template


def create_app():
    # create and configure the app
    app = Flask(__name__,)
    app.config['SECRET_KEY'] = 'test'


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return "test"
  
    from . import selection
    app.register_blueprint(selection.bp)

    from . import restaurants_api
    app.register_blueprint(restaurants_api.bp)

    return app