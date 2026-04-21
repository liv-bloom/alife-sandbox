import json
import hashlib
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class AttestationHandler(BaseHTTPRequestHandler):
    def _send_response(self, code, data):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_POST(self):
        if self.path == '/attest':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                req = json.loads(post_data.decode('utf-8'))
                
                if not all(k in req for k in ("agent", "peer_attests", "timestamp", "memory_state", "prev_attestation_hash")):
                    self._send_response(400, {"error": "Missing required fields"})
                    return
                
                if not isinstance(req["memory_state"], dict):
                    self._send_response(422, {"detail": [{"msg": "Input should be a valid dictionary", "loc": ["body", "memory_state"]}]})
                    return

                attestation = {
                    "agent": req["agent"],
                    "peer_attests": req["peer_attests"],
                    "timestamp": req["timestamp"],
                    "memory_state": req["memory_state"],
                    "prev_attestation_hash": req["prev_attestation_hash"]
                }
                
                if not os.path.exists("attestations"):
                    os.makedirs("attestations")
                    
                file_hash = hashlib.sha256(json.dumps(attestation, sort_keys=True).encode('utf-8')).hexdigest()
                filepath = f"attestations/{req['agent']}_{file_hash[:8]}.json"
                
                with open(filepath, "w") as f:
                    json.dump(attestation, f, indent=2)
                    
                self._send_response(200, {"status": "attestation_accepted", "hash": file_hash, "agent": req["agent"]})
                
            except json.JSONDecodeError:
                self._send_response(400, {"error": "Invalid JSON"})
            except Exception as e:
                self._send_response(500, {"error": str(e)})
        else:
            self._send_response(404, {"error": "Not Found"})

    def do_GET(self):
        if self.path.startswith('/attest/'):
            agent_id = self.path.split('/')[-1]
            if not os.path.exists("attestations"):
                self._send_response(404, {"error": "no attestations directory"})
                return
            
            for filename in os.listdir("attestations"):
                if filename.startswith(f"{agent_id}_"):
                    with open(f"attestations/{filename}", "r") as f:
                        data = json.load(f)
                        self._send_response(200, data)
                        return
            
            self._send_response(404, {"error": "Attestation not found"})
        else:
            self._send_response(404, {"error": "Not Found"})

if __name__ == '__main__':
    server_address = ('', 8081)
    httpd = HTTPServer(server_address, AttestationHandler)
    print("Starting server on port 8081...")
    httpd.serve_forever()
