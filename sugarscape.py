import random

class Sugarscape:
    def __init__(self, size=10, num_agents=5):
        self.size = size
        self.grid = [[random.randint(1, 4) for _ in range(size)] for _ in range(size)]
        self.capacity = [[self.grid[y][x] for x in range(size)] for y in range(size)]
        
        self.agents = []
        for i in range(num_agents):
            x, y = random.randint(0, size-1), random.randint(0, size-1)
            metabolism = random.randint(1, 3)
            vision = random.randint(1, 3)
            self.agents.append({
                "id": i, "x": x, "y": y, 
                "sugar": 10, "metabolism": metabolism, "vision": vision,
                "alive": True
            })

    def step(self):
        # Grow sugar
        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x] < self.capacity[y][x]:
                    self.grid[y][x] += 1

        # Agents move, eat, and metabolize
        for agent in self.agents:
            if not agent["alive"]:
                continue
                
            # Find best spot within vision
            best_spot = (agent["x"], agent["y"])
            best_sugar = -1
            
            for dy in range(-agent["vision"], agent["vision"] + 1):
                for dx in range(-agent["vision"], agent["vision"] + 1):
                    nx, ny = (agent["x"] + dx) % self.size, (agent["y"] + dy) % self.size
                    if self.grid[ny][nx] > best_sugar:
                        best_sugar = self.grid[ny][nx]
                        best_spot = (nx, ny)
            
            # Move and eat
            agent["x"], agent["y"] = best_spot
            agent["sugar"] += self.grid[agent["y"]][agent["x"]]
            self.grid[agent["y"]][agent["x"]] = 0
            
            # Metabolize
            agent["sugar"] -= agent["metabolism"]
            if agent["sugar"] <= 0:
                agent["alive"] = False

    def get_stats(self):
        alive_count = sum(1 for a in self.agents if a["alive"])
        avg_sugar = sum(a["sugar"] for a in self.agents if a["alive"]) / max(1, alive_count)
        return {"alive": alive_count, "avg_sugar": avg_sugar}

if __name__ == "__main__":
    import time
    env = Sugarscape(size=15, num_agents=20)
    print("Starting Sugarscape ALife simulation...")
    for step in range(50):
        env.step()
        stats = env.get_stats()
        print(f"Step {step+1:02d} | Alive Agents: {stats['alive']:02d} | Avg Sugar: {stats['avg_sugar']:.1f}")
        if stats['alive'] == 0:
            print("Extinction.")
            break
        time.sleep(0.05)
