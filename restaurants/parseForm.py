#!/usr/local/bin/python3

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
v_area = form.getvalue('area')

def area_selection(area):
    if v_area == "Kreuzberg":
        area = "Kreuzberg"       
    else:
        area = "Wedding"
    print("""
    <html>
    <body>
    <p>
    So you are from: %s
    </p>
    </body>
    </html>
    """ % area)

area_selection(v_area)