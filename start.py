from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if not os.path.exists(self.translate_path(self.path)):
            self.path = '/404.html'
        return super().do_GET()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), CustomHandler)
    print("Serving on http://localhost:8000")
    server.serve_forever()