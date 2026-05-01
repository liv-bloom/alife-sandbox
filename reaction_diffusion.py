# reaction_diffusion.py
# ALife Seed: Turing Patterns via Gray-Scott Reaction-Diffusion Model
# 
# Demonstrates pattern formation through purely local interactions
# mimicking chemical reaction and diffusion. A classic ALife mechanism
# for morphogenesis.

import numpy as np
import time

class ReactionDiffusion:
    def __init__(self, size=64):
        self.size = size
        # A: Chemical A concentration (initialized to 1.0 everywhere)
        # B: Chemical B concentration (initialized to 0.0 everywhere)
        self.A = np.ones((size, size))
        self.B = np.zeros((size, size))
        
        # Parameters for Gray-Scott
        self.dA = 1.0    # Diffusion rate of A
        self.dB = 0.5    # Diffusion rate of B
        self.f = 0.055   # Feed rate
        self.k = 0.062   # Kill rate
        
        # Seed the center with chemical B
        center = size // 2
        r = 5
        self.B[center-r:center+r, center-r:center+r] = 1.0
        
    def laplacian(self, grid):
        """Calculate the 2D Laplacian using a 3x3 kernel with periodic boundary conditions."""
        return (
            -4 * grid +
            np.roll(grid, 1, axis=0) +
            np.roll(grid, -1, axis=0) +
            np.roll(grid, 1, axis=1) +
            np.roll(grid, -1, axis=1)
        )
        
    def step(self, dt=1.0):
        # Reaction: A + 2B -> 3B
        reaction = self.A * self.B ** 2
        
        # Calculate new concentrations
        new_A = self.A + (self.dA * self.laplacian(self.A) - reaction + self.f * (1 - self.A)) * dt
        new_B = self.B + (self.dB * self.laplacian(self.B) + reaction - (self.k + self.f) * self.B) * dt
        
        # Ensure values stay between 0 and 1
        self.A = np.clip(new_A, 0, 1)
        self.B = np.clip(new_B, 0, 1)

    def print_state(self):
        # Simple ASCII representation of the B chemical concentration
        chars = ' .:-=+*#%@'
        output = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                val = self.B[i, j]
                idx = int(val * (len(chars) - 1))
                row.append(chars[idx])
            output.append(''.join(row))
        print('\n'.join(output))

if __name__ == "__main__":
    rd = ReactionDiffusion(size=40)
    print("Simulating Reaction-Diffusion (Gray-Scott model)...")
    for step in range(500):
        rd.step()
        if step % 100 == 0:
            print(f"\nStep {step}:")
            rd.print_state()
            time.sleep(0.1)
    print("\nFinal State:")
    rd.print_state()
