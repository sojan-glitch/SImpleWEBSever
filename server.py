
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

server = HTTPServer(("127.0.0.1", PORT), SimpleHTTPRequestHandler)

print(f"Server started at http://127.0.0.1:{PORT}")

server.serve_forever()