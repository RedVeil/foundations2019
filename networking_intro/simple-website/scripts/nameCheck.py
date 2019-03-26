#!/usr/local/bin/python3

import cgi
# get the output of the form.

form = cgi.FieldStorage()
v_name = form.getvalue("name")

print(
"""
<html>
<head>
  <link href="/style.css" rel="stylesheet">
</head>
<body>
<div class="navbar">
  <a href="index.html">Home</a>
  <a href="page2.html">Page2</a>
  <a href="page3.html">Page3</a>
</div>
<p>
Thanks, %s
</p>
</body>
</html>
""" % v_name
)
