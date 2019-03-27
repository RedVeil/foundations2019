from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp = Blueprint('restaurants', __name__,url_prefix='/restaurants')

@bp.route('/list')
def show(page):
    try:
        return render_template("restaurants/list.html")
    except TemplateNotFound:
        abort(404)