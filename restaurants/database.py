## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

# import the python library for SQLite 
import sqlite3

argument = "WHERE NEIGHBORHOOD_ID = 1"

def __init__():
    db_connection = sqlite3.connect('my_restaurants.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT * from restaurants {argument}")
    list_restaurants = db_cursor.fetchall()
    return(list_restaurants)

print(__init__())