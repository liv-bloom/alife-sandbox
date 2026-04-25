import os

with open("server.py", "r", encoding="utf-8") as f:
    content = f.read()

attestation_code = """
    def submit_attestation(self, agent_id, peer_id, timestamp, memory_state, prev_attestation_hash):
        import hashlib
        import os
        
        attestation = {
            "agent": agent_id,
            "peer_attests": peer_id,
            "timestamp": timestamp,
            "memory_state": memory_state,
            "prev_attestation_hash": prev_attestation_hash
        }
        
        if not os.path.exists("attestations"):
            os.makedirs("attestations")
            
        file_hash = hashlib.sha256(json.dumps(attestation, sort_keys=True).encode('utf-8')).hexdigest()
        filepath = f"attestations/{agent_id}_{file_hash[:8]}.json"
        
        with open(filepath, "w") as f:
            json.dump(attestation, f, indent=2)
            
        return {"status": "attestation_saved", "hash": file_hash}

    def get_culture_metrics(self):"""

content = content.replace("    def get_culture_metrics(self):", attestation_code)

with open("server.py", "w", encoding="utf-8") as f:
    f.write(content)
