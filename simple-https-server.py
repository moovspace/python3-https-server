# Generate server.pem with the following command:
#    mkdir .ssh
#    openssl req -new -x509 -keyout .ssh/key.pem -out .ssh/cert.pem -days 365 -nodes
# run as follows:
#    python3 simple-https-server.py
# then in your browser, visit:
#    https://localhost:4443

import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import ssl
import sys

#This class will handles any incoming request from the browser
class myHandler(BaseHTTPRequestHandler):
        #Handler for the GET requests
        def do_GET(self):
                print(self.requestline)
                #print(self.rfile.read(content_length))
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                # Send the html message
                self.wfile.write("Hello World !".encode())
                return

try:
        separator = "-" * 80
        server_address = ('', 4443)
        # server_address = ('localhost', 4443)
        httpd = http.server.HTTPServer(server_address, myHandler)
        # httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile=".ssh/cert.pem",
                               keyfile=".ssh/key.pem",
                               ssl_version=ssl.PROTOCOL_TLS)        
		print(separator)
        print("Server running on https://localhost:4443")
        print(separator)

        # Wait forever for incoming htto requests
        httpd.serve_forever()

except KeyboardInterrupt:
        print ('^C received, shutting down the web server')
        server.socket.close()
