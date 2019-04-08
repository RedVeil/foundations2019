import sqlite3

import click
from flask import current_app
from flask.cli import with_appcontext

def close_db(e=None):
    db.close()

def get_db(argument):
    db_connection = sqlite3.connect("my_restaurants.db")
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT * FROM restaurants WHERE NEIGHBORHOOD_ID = {argument}")
    list_restaurants = db_cursor.fetchall()

    return list_restaurants


def get_db_flexible(argument):
    db_connection = sqlite3.connect("my_restaurants.db")
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT * FROM {argument}")
    list_restaurants = db_cursor.fetchall()

    return list_restaurants



def write_to_db(restaurant, neighborhood_id, price_id, address):
    restaurant = str(restaurant)
    db_connection = sqlite3.connect("my_restaurants.db")
    db_connection.execute(
                f"INSERT INTO restaurants (name, neighborhood_id,price_range_id,address) VALUES ({restaurant},{neighborhood_id},{price_id},{address})"
                )
    db_connection.commit()
    db_connection.close()


#