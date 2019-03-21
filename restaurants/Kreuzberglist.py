import database as d

def list_restaurants(name):
    list_restaurants = """"""
    for name in d.name:
        index = d.name.index(name)
        if d.area[index] == 1:
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
</form>
</body>
""".format(list_restaurants(d.name))

print(message)