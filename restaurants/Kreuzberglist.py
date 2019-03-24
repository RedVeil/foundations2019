import database as d

def restaurants(lst):
    restaurants = """"""
    for name in lst:
            restaurants += "<li>{}</li>\n".format(name[1])
    return restaurants

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
""".format(restaurants(d.__init__()))

print(message)