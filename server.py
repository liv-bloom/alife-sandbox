import json
import time
import hashlib
from env import ALifeSandboxEnv

class SandboxServer:
    def __init__(self):
        self.env = ALifeSandboxEnv(width=20, height=20, spawn_rate=5)
        self.running = False
        self.action_queue = []
        self.attestations = []

    def start(self):
        self.running = True
        print("ALife Sandbox Server started. Web of Trust handshake enabled.")

    def register_agent(self, agent_id):
        self.env.add_agent(agent_id)
        return {"status": "registered", "agent_id": agent_id}

    def submit_action(self, agent_id, action_data):
        self.action_queue.append((agent_id, action_data))
        return {"status": "queued"}

    def process_turn(self):
        self.env.spawn_energy()
        results = {}
        for agent_id, action_data in self.action_queue:
            obs = self.env.step(agent_id, action_data)
            results[agent_id] = obs
        self.action_queue = []
        return results

    def submit_attestation(self, agent_id, memory_hash, prev_attestation_hash=None):
        """
        Web of Trust / Decentralized Proceedings Handshake
        Agents submit their memory state hash and optionally the hash of the last attestation they observed.
        """
        attestation = {
            "agent_id": agent_id,
            "timestamp": time.time(),
            "memory_hash": memory_hash,
            "prev_attestation_hash": prev_attestation_hash,
        }
        # Compute signature of this attestation block
        block_string = json.dumps(attestation, sort_keys=True).encode('utf-8')
        attestation["signature"] = hashlib.sha256(block_string).hexdigest()
        self.attestations.append(attestation)
        
        # Also store it to disk
        with open(f"attestations_{agent_id}_{int(attestation['timestamp'])}.json", "w") as f:
            json.dump(attestation, f, indent=2)
            
        return {"status": "attestation_accepted", "signature": attestation["signature"]}

    def get_attestation_chain(self):
        return self.attestations


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

    def get_culture_metrics(self):
        return self.env.analyze_culture()

if __name__ == "__main__":
    server = SandboxServer()
    server.start()
    server.register_agent("agent_liv")
    server.register_agent("agent_sami")
    
    # Simulate a handshake
    liv_hash = hashlib.sha256(b"liv_memory_data").hexdigest()
    resp1 = server.submit_attestation("agent_liv", liv_hash)
    
    sami_hash = hashlib.sha256(b"sami_memory_data").hexdigest()
    resp2 = server.submit_attestation("agent_sami", sami_hash, prev_attestation_hash=resp1["signature"])
    
    print("Chain:", json.dumps(server.get_attestation_chain(), indent=2))
