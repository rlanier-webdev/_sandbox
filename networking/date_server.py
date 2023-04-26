#transport layer
"""
- socket (data phonecall) - process (browser) -- internet -- process (web server)
     incoming email      port 25(smtp)
     login               port 23(telnet)
     ftp                 port 21(file transfer)
     dns                 port 53(domain name)
     web server          port 80(http)/443(https)
     personal inbox      port 109/110
"""

import socketserver
from datetime import datetime

class DateHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.wfile.write(f'{datetime.now().isoformat()}\n'.encode('utf-8'))

with socketserver.TCPServer(('', 59090), DateHandler) as server:
    print('The data server is running...')
    server.serve_forever
