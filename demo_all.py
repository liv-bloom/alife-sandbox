# demo_all.py
# A quick runner to demonstrate the ALife Sandbox seeds.

print("🌱 Welcome to the ALife Sandbox Demo 🌱\n")

print("1. Conway's Game of Life (Cellular Automata)")
try:
    import game_of_life
    grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    print("Generation 1:")
    for r in game_of_life.next_generation(grid): print(r)
except Exception as e: print("Error loading Game of Life:", e)
print()

print("2. L-System (Fractal Plant Growth)")
try:
    import lsystem
    plant_rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}
    print(f"Plant Iteration 1: {lsystem.generate_lsystem('X', plant_rules, 1)}")
except Exception as e: print("Error loading L-System:", e)
print()

print("3. Boids (Flocking Simulation)")
try:
    import boids
    boids.simulate_boids(steps=2)
except Exception as e: print("Error loading Boids:", e)
print()

print("To see Toroidal Bounded Coordination (env.py) or AOW Cryptographic Attestation (pulse.py), please run their respective modules directly.")
print("Thank you for visiting the garden.")
