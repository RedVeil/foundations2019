import functools
import urllib.request as request
from flask import (
    Blueprint, flash, g, redirect, render_template, session, url_for)

bp = Blueprint("dogs", __name__)




def get_doggie():
    content = request.urlopen("https://dog.ceo/api/breeds/image/random").read()
    content = content.decode("UTF-8")
    img = content[content.find("https"):-2]
    return img

@bp.route("/dogs")
def start():
    url = get_doggie()
    return render_template("dogs.html", url = url)
    print(url)
