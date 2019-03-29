import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from db import get_db

bp = Blueprint("selection", __name__)


class SelectionForm(FlaskForm):
    area = RadioField("area", choices = [('1','Kreuzberg'),('2','Wedding'),('3','Neukölln'),('4','Spandau'),('5','Mitte')])
    submit = SubmitField("Send")


def create_message(lst):
    restaurants =[]
    for name in lst:
        restaurants.append("{}".format(name[1]))
    return restaurants
      
@bp.route("/choice", methods=("GET", "POST"))
def test():
    form = SelectionForm()
    if request.method == "POST":
        list_restaurants = get_db(form.area.data)
        message = create_message(list_restaurants)
        return render_template("restaurants_list.html", message = message)
    return render_template('choice.html', form= form)





