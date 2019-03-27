import sqlite3

import click
from flask import current_app
from flask.cli import with_appcontext

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def get_db(argument):
    db_connection = sqlite3.connect("my_restaurants.db")
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT * FROM restaurants WHERE NEIGHBORHOOD_ID = {argument}")
    list_restaurants = db_cursor.fetchall()

    return list_restaurants