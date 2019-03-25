#!/usr/local/bin/python3
import sqlite3
import cgi
#import database as d


form = cgi.FieldStorage()
v_area = form.getvalue("area")
#v_area = 1

def get_database(v_area):
    db_connection = sqlite3.connect('my_restaurants.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * FROM restaurants WHERE NEIGHBORHOOD_ID ={}".format(v_area))
    list_restaurants = db_cursor.fetchall()
    return(list_restaurants)


def restaurants(lst):
    restaurants = """"""
    for name in lst:
            restaurants += "<li>{}</li>\n".format(name[1])
    return restaurants

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
""".format(restaurants(get_database(v_area)))
)
