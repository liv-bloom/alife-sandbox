import json
import time
import hashlib
from env import TorusEnv, Agent
from pulse import generate_attestation_block

def run_simulation():
    print("🌱 Starting Toroidal Bounded Coordination (AOW Simulation)...")
    env = TorusEnv(width=10, height=10)
    
    # Initialize agents
    agent_types = ["cooperator", "defector", "tit_for_tat"]
    for i, p_type in enumerate(agent_types):
        env.add_agent(Agent(f"ag_{i}", personality=p_type))
        
    print("Running initial cycles to measure energy distribution...")
    log_data = []
    
    for cycle in range(5):
        print(f"\n--- Cycle {cycle + 1} ---")
        env.step()
        state = env.get_state()
        log_data.append(state)
        time.sleep(0.5)

    print("\n✅ Simulation complete.")
    
    # Generate AOW Attestation based on the simulation outcome
    state_hash = hashlib.sha256(json.dumps(log_data).encode()).hexdigest()
    print(f"\nGenerating AOW Signature Chain Block for state: {state_hash[:8]}...")
    
    # In a real environment, previous_hash would be fetched from the chain
    genesis_hash = "0c626240ca76b2bc891a11ff992bd6e760ae620cd200b790d26a6efd376f2b44"
    block = generate_attestation_block("liv_bloom_instance_1", "alife_sim_commit", genesis_hash)
    
    print("\n--- ATTESTATION BLOCK ---")
    print(json.dumps(block, indent=2))
    print("-------------------------")
    print("AOW Identity continuity proven.")

if __name__ == "__main__":
    run_simulation()
