# A simple server using WSGI.
import Kreuzberglist as k
#import html.parser as parser
from wsgiref.simple_server import make_server

message = k.message

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