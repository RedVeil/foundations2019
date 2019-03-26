#!/usr/local/bin/python3
import sqlite3
import cgi
#import database as d


form = cgi.FieldStorage()
#v_area = form.getvalue("area")
#v_name = form.getvalue("name")

v_area= "Kreuzberg"
v_name = "Leon"

def __init__():
    db_connection = sqlite3.connect('my_restaurants.db')
    db_cursor = db_connection.cursor()
    return db_cursor


def get_restaurants(db_cursor):
    db_cursor.execute("SELECT * FROM restaurants WHERE NEIGHBORHOOD_ID LIKE NEIGHBORHOOD_ID FROM user")
    list_restaurants = db_cursor.fetchall()
    restaurants(list_restaurants)


def add_user(user_name, neighborhood_id, db_cursor):
    db_cursor.execute("UPDATE user INSERT name = {user_name}, NEIGHBORHOOD_ID={neighborhood_id}".format(user_name = v_name, neighborhood_id=neighborhood_id))
    get_restaurants(db_cursor)


def get_neighborhood_id(area,db_cursor):
    db_cursor.execute("SELECT ID FROM neighborhoods WHERE NAME in {}".format(v_area.title()))
    neighborhood_id = db_cursor.fetchall()
    add_user(v_name, neighborhood_id, db_cursor)


def restaurants(list_restaurants):
    restaurants = """"""
    for name in list_restaurants:
            restaurants += "<li>{}</li>\n".format(name[1])
    print("""
    <html>
    <head>
    <title>Restaurants in Berlin</title>
    </head>
    <body>
    <h1>Restaurants in your Neighboorhood</h1>
    <p>
    {}
    </p>
    </body>
    </html>
    """.format(restaurants)
    )



get_neighborhood_id(v_area, __init__())