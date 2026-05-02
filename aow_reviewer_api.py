from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import subprocess
import tempfile
import os

class AOWReviewHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/aow/review':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                
                # Write to temp file
                fd, temp_path = tempfile.mkstemp(suffix=".json")
                with os.fdopen(fd, 'w') as f:
                    json.dump(data, f)
                
                # Run the reviewer script
                result = subprocess.run(['python3', '/home/masumori/.openclaw/workspace-liv/projects/alife-sandbox/aow_reviewer.py', temp_path], capture_output=True, text=True)
                
                # Cleanup
                os.remove(temp_path)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                response = {
                    "status": "success",
                    "reviewer": "AOW AI Reviewer (v0.2)",
                    "log": result.stdout
                }
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=AOWReviewHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting AOW Review API server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
