from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            try:
                # Construct the full path to the HTML file
                script_dir = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(script_dir, 'Services', 'localhost_html', 'test.html')

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"File not found")

# Start the server
if __name__ == "__main__":
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, Serv)
    print("Server running at http://localhost:8080/")
    httpd.serve_forever()