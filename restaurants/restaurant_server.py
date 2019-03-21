# A simple server using WSGI.
import test as t
#import html.parser as parser
from wsgiref.simple_server import make_server

message = """
<html>
<head>
  <title>test</title>
</head>
<body>

<p>
  test
</p>
<form action="/parseForm.py" method="post">
  <label for="area">Your Area: </label>
  <input type="radio" id="area" value="1">Kreuzberg<br>
  <input type="radio" id="area" value="2">Wedding<br>
  <input type="radio" id="area" value="3">Neukölln<br>
  <input type="radio" id="area" value="4">Spandau<br>
  <input type="submit" value="Send">
</form>
</body>
</html>

"""

def simple_app(_environ, start_response):

    # set status and HTTP header for response, both needed.
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]

    start_response(status, headers)

    # HTML body to be rendered
    body = [message.encode("utf-8")]

    return body


# define server daemon
httpd = make_server('localhost', 8001, simple_app)
print("WSGI server on port 8000...")

# server
httpd.serve_forever()