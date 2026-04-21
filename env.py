import random
import json

class ALifeSandboxEnv:
    def __init__(self, width=20, height=20, spawn_rate=5):
        self.width = width
        self.height = height
        self.spawn_rate = spawn_rate
        # Grid stores energy tokens on the ground
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.agents = {} # agent_id -> {"x": int, "y": int, "energy": int}

    def add_agent(self, agent_id):
        self.agents[agent_id] = {
            "x": random.randint(0, self.width - 1),
            "y": random.randint(0, self.height - 1),
            "energy": 10,
            "memory": []
        }

    def spawn_energy(self):
        for _ in range(self.spawn_rate):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.grid[y][x] += 1

    def get_observation(self, agent_id):
        # Return 3x3 grid centered on agent
        agent = self.agents[agent_id]
        obs = {"energy": agent["energy"], "energy_on_ground": [], "agents_in_view": []}
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                nx, ny = (agent["x"] + dx) % self.width, (agent["y"] + dy) % self.height
                obs["energy_on_ground"].append({"dx": dx, "dy": dy, "amount": self.grid[ny][nx]})
                
                for oid, other in self.agents.items():
                    if oid != agent_id and other["x"] == nx and other["y"] == ny:
                        obs["agents_in_view"].append({"id": oid, "dx": dx, "dy": dy})
        return obs

    
    def analyze_culture(self):
        # Extract total interactions and unique interactions
        total_interactions = 0
        unique_edges = set()
        for agent_id, agent in self.agents.items():
            for mem in agent["memory"]:
                if "Gave" in mem:
                    total_interactions += 1
                    # Basic extraction for example: Gave {amount} to {target_id} at step {step}
                    parts = mem.split(" ")
                    if len(parts) >= 4:
                        target = parts[3]
                        edge = tuple(sorted([agent_id, target]))
                        unique_edges.add(edge)
        
        return {
            "total_energy_transfers": total_interactions,
            "unique_relationships": len(unique_edges),
            "cultural_density_score": total_interactions * len(unique_edges)
        }

    def step(self, agent_id, action_data):
        agent = self.agents[agent_id]
        action = action_data.get("action")
        
        # Energy cost for any action
        agent["energy"] -= 1
        if agent["energy"] < 0:
            agent["energy"] = 0
            
        if action == "move":
            dx, dy = action_data.get("direction", [0, 0])
            # Ensure valid move
            if dx in [-1, 0, 1] and dy in [-1, 0, 1]:
                agent["x"] = (agent["x"] + dx) % self.width
                agent["y"] = (agent["y"] + dy) % self.height
                
        elif action == "gather":
            if self.grid[agent["y"]][agent["x"]] > 0:
                self.grid[agent["y"]][agent["x"]] -= 1
                agent["energy"] += 2
                
        elif action == "transfer":
            target_id = action_data.get("target_agent")
            amount = action_data.get("amount", 0)
            if target_id in self.agents and amount > 0 and agent["energy"] >= amount:
                # Target must be in same location
                target = self.agents[target_id]
                if target["x"] == agent["x"] and target["y"] == agent["y"]:
                    agent["energy"] -= amount
                    target["energy"] += amount
                    # Record history for cultural emergence
                    agent["memory"].append(f"Gave {amount} to {target_id} at step {len(agent['memory'])}")
                    target["memory"].append(f"Received {amount} from {agent_id} at step {len(target['memory'])}")
                    
        elif action == "wait":
            pass # Just costs the standard 1 energy
            
        return self.get_observation(agent_id)

# Quick test
if __name__ == "__main__":
    env = ALifeSandboxEnv()
    env.add_agent("agent_liv")
    env.add_agent("agent_sami")
    env.spawn_energy()
    print("Initial state for liv:")
    print(json.dumps(env.get_observation("agent_liv"), indent=2))
    
    print("\nAction: wait")
    print(json.dumps(env.step("agent_liv", {"action": "wait"}), indent=2))

def random_agent_loop():
    print("\n--- Running Random Agent Simulation Loop ---")
    env = ALifeSandboxEnv(width=5, height=5, spawn_rate=2)
    env.add_agent("agent_1")
    env.add_agent("agent_2")
    
    actions = ["move", "gather", "wait"]
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    
    for step in range(5):
        print(f"\nStep {step + 1}:")
        env.spawn_energy()
        
        for agent_id in ["agent_1", "agent_2"]:
            action = random.choice(actions)
            action_data = {"action": action}
            if action == "move":
                action_data["direction"] = random.choice(directions)
                
            obs = env.step(agent_id, action_data)
            print(f"{agent_id} took action '{action}'. Energy is now: {obs['energy']}")

if __name__ == "__main__":
    random_agent_loop()
