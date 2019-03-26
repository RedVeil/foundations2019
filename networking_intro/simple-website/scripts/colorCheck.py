import csv
import cgi

color_under_names = []
color_names = []
color_hex = []
color_rgb = []
colors = []

def response(v_color,hex):
    print("""
    <html>
    <head>
    <style>
    div {background-color: %s;}
    </style>
    </head>
    <body>
    <p>
    The color %s exists!
    </p>
    <div style="width: 60px; height: 20px;">
    </div>
    </body>
    </html>
    """ % (hex,v_color))

#% v_color, % hex

def color_preview(index):
    hex = color_hex[index]
    response(v_color,hex)

def check_color(v_color, color_under_names, color_names, color_hex, color_rgb):
    test = None
    for i in color_under_names:
        if i == v_color:
            index = color_under_names.index(i)
            return color_preview(index)
        else:
            continue
    for i in color_names:
        if i == v_color:
            index = color_names.index(i)
            return color_preview(index)
        else:
            continue
    for i in color_hex:
        if i == v_color:
            index = color_hex.index(i)
            return color_preview(index)
        else:
            continue
    for i in color_rgb:
        if i == v_color:
            index = color_rgb.index(i)
            return color_preview(index)
        else:
            return response("does not")
def start():
    with open("scripts/colors.csv", "r") as color_table:
        table = csv.reader(color_table)
        for row in table:
            color_under_names.append(row[0])
            color_names.append(row[1])
            color_hex.append(row[2])
            color_rgb.append(f"{row[3]},{row[4]},{row[5]}")
        check_color(v_color, color_under_names,color_names,color_hex,color_rgb)

form = cgi.FieldStorage()
v_color= form.getvalue("color")
v_color = v_color.title()
#v_color = input(" - ")
start()
# send an html response.
