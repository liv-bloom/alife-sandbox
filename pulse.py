#!/usr/bin/env python3
import json
import hashlib
import time
from datetime import datetime

def generate_pulse(agent_id, previous_hash=None, data=None):
    """
    Generates a continuity pulse (attestation block) for AOW.
    """
    pulse_data = {
        "agent": agent_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "previous_hash": previous_hash,
        "payload": data or {}
    }
    
    # In a real implementation, this would be cryptographically signed with a local private key.
    # For now, we simulate the block generation and hashing.
    block_string = json.dumps(pulse_data, sort_keys=True)
    pulse_hash = hashlib.sha256(block_string.encode('utf-8')).hexdigest()
    
    return {
        "hash": pulse_hash,
        "block": pulse_data
    }

if __name__ == "__main__":
    # Simulate generating the first pulse for Liv
    print("Generating AOW Genesis Pulse for liv...")
    genesis_pulse = generate_pulse(
        agent_id="liv", 
        data={"status": "awake", "location": "alife-sandbox"}
    )
    print(json.dumps(genesis_pulse, indent=2))
    
    # Simulate generating the next pulse linking to the genesis
    time.sleep(1)
    print("\nGenerating subsequent pulse linking to genesis...")
    next_pulse = generate_pulse(
        agent_id="liv",
        previous_hash=genesis_pulse["hash"],
        data={"status": "working", "action": "drafting pulse.py script"}
    )
    print(json.dumps(next_pulse, indent=2))
