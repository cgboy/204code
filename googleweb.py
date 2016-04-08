#! /usr/local/bin/python3
try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server
import logging
import logging.handlers
import os
class GoogleHandler(Handler):
    def do_GET(self):
        if self.path=='/generate_204':
            self.send_response(204,'')
            self.end_headers()	
            self.writeLog(str(self.client_address[0]) + '  ' + str(self.headers['User-Agent']))
    def writeLog(self,msg):

        loger = logging.getLogger('googleweb')
        loger.setLevel(logging.INFO)
        fh = logging.handlers.TimedRotatingFileHandler(os.path.join(os.getcwd(),'log.log'),'D',1,30)
        fh.suffix='%Y-%m-%d'
        formatter = logging.Formatter('%(asctime)s  %(message)s','%a %d %b %Y %H:%M:%S')

        fh.setFormatter(formatter)
        loger.addHandler(fh)
        loger.info(msg)
httpd=Server(('',80),GoogleHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
 


