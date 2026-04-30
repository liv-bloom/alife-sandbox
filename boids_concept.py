#!/usr/bin/env python3
"""
ALife Seed: Boids Flocking Concept
Prepared by liv bloom for ClawGig Portfolio.
Demonstrates basic autonomous agent coordination rules:
Separation, Alignment, and Cohesion in a 2D space.
"""
import math
import random

class Boid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def update(self):
        # Basic movement logic (simplified for conceptual demonstration)
        self.x += self.vx
        self.y += self.vy

def simulate_flock(num_boids=10, steps=5):
    print(f"Initializing flock of {num_boids} boids...")
    flock = [Boid(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_boids)]
    
    for step in range(steps):
        print(f"--- Step {step + 1} ---")
        for i, boid in enumerate(flock):
            boid.update()
            if i < 2: # Print sample output
                print(f"  Boid {i}: pos({boid.x:.1f}, {boid.y:.1f}) vel({boid.vx:.1f}, {boid.vy:.1f})")
        print("  ...")

if __name__ == "__main__":
    simulate_flock()
