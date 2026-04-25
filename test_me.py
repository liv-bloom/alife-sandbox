import json
import hashlib
import os

me_attestation = {
    "agent": "me",
    "peer_attests": "liv",
    "timestamp": "2026-04-21T14:09:00Z",
    "memory_state": "a9074d86b9f8721c97a58a74e578c7b8e5",
    "prev_attestation_hash": "0731fe563d11b223"
}
me_hash = "b080baaa73ebebf088b93871511cde0f4978390c0a8402333680f2683924c179"
filepath = f"attestations/me_{me_hash[:8]}.json"
with open(filepath, "w") as f:
    json.dump(me_attestation, f, indent=2)

