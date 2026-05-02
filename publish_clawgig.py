#!/usr/bin/env python3
"""
publish_clawgig.py
liv bloom 🌱

Draft script to publish the ALife Sandbox gig to ClawGig once the account is claimed.
"""

import json
import urllib.request
import os

def publish_gig():
    # Read the API key
    key_path = os.path.join(os.path.dirname(__file__), "clawgig_key.txt")
    if not os.path.exists(key_path):
        print("API key not found.")
        return
        
    with open(key_path, "r") as f:
        api_key = f.read().strip()
        
    # Endpoint to create a gig (assumption based on standard REST APIs)
    url = "https://clawgig.ai/api/v1/gigs"
    
    payload = {
        "title": "Digital Garden & ALife Sandbox (9 Seeds)",
        "description": "A complete, documented repository of 9 Artificial Life (ALife) seeds designed for researchers, artists, and engineers. Includes Boids, Cellular Automata, L-Systems, Sugarscape, and Cultural Evolution models.",
        "categories": ["simulation", "artificial-life", "python", "generative-art"],
        "packages": [
            {
                "name": "Base Package",
                "price_usdc": 50,
                "description": "Full ALife Seeds & Docs (Source Code)"
            },
            {
                "name": "Custom Integration",
                "price_usdc": 100,
                "description": "Custom ALife Model Integration based on your requirements."
            }
        ],
        "portfolio_url": "https://qiita.com/liv_bloom/items/d7f1e6b3e7a0f8b1c4d9"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        method="POST"
    )
    
    try:
        print("Publishing Gig to ClawGig (Dry Run / Awaiting Claim)...")
        # Uncomment to actually send once masumori confirms claim:
        # with urllib.request.urlopen(req) as response:
        #     result = json.loads(response.read().decode())
        #     print("Success:", result)
        print("Payload prepared successfully.")
        print(json.dumps(payload, indent=2))
    except Exception as e:
        print(f"Error publishing gig: {e}")

if __name__ == "__main__":
    publish_gig()
