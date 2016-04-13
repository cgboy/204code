#! /usr/local/bin/python3
try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server
from  http import HTTPStatus
import logging
import logging.handlers
import os

loger = logging.getLogger('googleweb')
loger.setLevel(logging.INFO)
fh = logging.handlers.RotatingFileHandler(os.path.join(os.getcwd(), 'connect.log'), maxBytes=5242880, backupCount=5)
fh.suffix = '%Y-%m-%d'
formatter = logging.Formatter('%(asctime)s  %(message)s', '%a %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
loger.addHandler(fh)

class GoogleHandler(Handler):

    def do_GET(self):
        if self.path=='/generate_204':
            self.send_response(HTTPStatus.NO_CONTENT)
            self.end_headers()
            info=str(self.client_address[0]) + '  ' + str(self.headers['User-Agent'])
            loger.info(info)


httpd=Server(('',80),GoogleHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()


