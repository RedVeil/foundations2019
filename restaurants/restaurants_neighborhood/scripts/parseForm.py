#!/usr/local/bin/python3

import cgi
#import database as d


form = cgi.FieldStorage()
v_area = form.getvalue("area")


'''def list_restaurants(name,area):
    list_restaurants = """"""
    for name in d.name:
        index = d.name.index(name)
        if d.area[index] == area:
            list_restaurants += "<li>{}</li>\n".format(name)
    return list_restaurants'''

print("""
<html>
<head>
  <title>Restaurants in Berlin</title>
</head>
<body>
<h1>Restaurants in Kreuzberg</h1>
<p>
test, %s
</p>
</body>
</html>
""" % v_area
)
