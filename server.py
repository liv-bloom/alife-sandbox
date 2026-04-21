import json
import time
from env import ALifeSandboxEnv

class SandboxServer:
    def __init__(self):
        self.env = ALifeSandboxEnv(width=20, height=20, spawn_rate=5)
        self.running = False
        self.action_queue = []

    def start(self):
        self.running = True
        print("ALife Sandbox Server started. Waiting for agents...")

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

    def get_culture_metrics(self):
        return self.env.analyze_culture()

if __name__ == "__main__":
    server = SandboxServer()
    server.start()
    server.register_agent("agent_liv")
    server.register_agent("agent_sami")
    print(server.submit_action("agent_liv", {"action": "wait"}))
    print("Turn results:", json.dumps(server.process_turn(), indent=2))
    print("Metrics:", server.get_culture_metrics())
