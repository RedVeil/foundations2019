### adapted from https://github.com/realpython/materials/tree/master/python-sockets-tutorial
## documentation at https://docs.python.org/3/library/socket.html
## more good info at https://docs.python.org/3/howto/sockets.html
from cgi import parse_qs, escape

def hello_world(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    if 'subject' in parameters:
        subject = escape(parameters['subject'][0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %s
    Hello %s!

''' % (subject,subject)]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, hello_world)
    srv.serve_forever()
