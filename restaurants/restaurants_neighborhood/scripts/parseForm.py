import cgi
import database as d


form = cgi.FieldStorage()
v_area = form.getvalue('area')


def list_restaurants(name,area):
    list_restaurants = """"""
    for name in d.name:
        index = d.name.index(name)
        if d.area[index] == v_area:
            list_restaurants += "<li>{}</li>\n".format(name)
    return list_restaurants

message = """
<head>
  <title>Restaurants in Berlin</title>
</head>
<body>
<h1>Restaurants in Kreuzberg</h1>
<ul>
{}
</ul>
</body>
""".format(list_restaurants(d.name,v_area))


print(message)