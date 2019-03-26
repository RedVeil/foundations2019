import http.server
import socketserver



handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/scripts"]

PORT = 2222
httpd =  socketserver.TCPServer(("127.0.0.1", PORT), handler)

httpd.server_name = "myServer"
httpd.server_port = PORT

print("serving at 127.0.0.1:", PORT)

httpd.serve_forever()
