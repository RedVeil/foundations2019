from flask import (Blueprint, render_template, abort,request)
from jinja2 import TemplateNotFound
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from db import get_db_flexible, write_to_db


bp = Blueprint('restaurants', __name__,url_prefix='/api/v1')

def create_message(lst,argument,argument2=None):
    message_list =[]
    for name in lst:
        message_list.append("{}".format(name[argument]))
        if argument2 != None:
            message_list.append(message_list.pop()+", {}".format(name[argument2]))
        else:
            continue
    return message_list


@bp.route('/restaurants')
def show():
    try:
        message = create_message(get_db_flexible("restaurants"),1,4)
        return render_template("/v1/restaurants.html", message = message)
    except TemplateNotFound:
        abort(404)

@bp.route('/neighborhoods')
def neighborhoods():
    try:
        message = create_message(get_db_flexible("neighborhoods"),1)
        return render_template("/v1/neighborhoods.html", message = message)
    except TemplateNotFound:
        abort(404)


class SelectionForm(FlaskForm):
    restaurant = StringField("restaurant")
    address = StringField("address")
    area = SelectField("area", choices = [('1','Kreuzberg'),('2','Wedding'),('3','Neukölln'),('4','Spandau'),('5','Mitte')])
    price = SelectField("price", choices = [('1','Cheap'),('2','Average'),('3','Pricey'),('4','Expensive'),('5','Crazy Expensive')])
    submit = SubmitField("Send")


def validator():
    pass

@bp.route('/add_restaurant', methods=("GET", "POST"))
def add_restaurant():
    form = SelectionForm()
    if request.method == "POST":
        write_to_db(form.restaurant.data, form.area.data, form.price.data, form.address.data)
        #message = create_message(get_db_flexible("restaurants"),1,4)
        #return render_template("/v1/add_restaurant.html", message=message)
        show()
    return render_template("/v1/add_restaurant.html", form=form)




