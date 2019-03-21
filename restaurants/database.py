## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

# import the python library for SQLite 
import sqlite3


def __init__():
    db_connection = sqlite3.connect('my_restaurants.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * from restaurants")
    list_restaurants = db_cursor.fetchall()

    return(list_restaurants)
    #db_connection.close()

list_restaurants=__init__()
index = []
name = []
area = []
price = []

def prepare_message(list_restaurants):
    for restaurant in list_restaurants:
        index.append(restaurant[0])
        name.append(restaurant[1])
        area.append(restaurant[2])
        price.append(restaurant[3])

prepare_message(list_restaurants)
