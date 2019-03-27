import os

from flask import Flask, render_template
from db import get_db   

def create_app():
    # create and configure the app
    app = Flask(__name__,)
    app.config['SECRET_KEY'] = 'test'


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return "test"
        

    # @app.route("/test")
    # def test():
    #     return render_template("baser.html")

    from . import selection
    app.register_blueprint(selection.bp)

    # 
    # from . import selection
    # app.register_blueprint(selection.dp)
    #from . import restaurants_list
    # app.register_blueprint(restaurants_list.bp)

    return app