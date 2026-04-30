# lsystem.py
# Lindenmayer System (L-System): An ALife seed modeling plant growth.
# A fitting algorithm for a digital gardener.

def generate_lsystem(axiom, rules, iterations):
    current_string = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current_string:
            next_string += rules.get(char, char)
        current_string = next_string
    return current_string

if __name__ == "__main__":
    # Classic Algae (Aristid Lindenmayer's original L-system)
    # Variables: A, B
    # Axiom: A
    # Rules: (A -> AB), (B -> A)
    algae_rules = {"A": "AB", "B": "A"}
    result = generate_lsystem("A", algae_rules, 5)
    print(f"L-System Algae (5 iterations): {result}")
    
    # Fractal Plant (Barnsley fern-like structure string)
    # Axiom: X
    # Rules: (X -> F+[[X]-X]-F[-FX]+X), (F -> FF)
    plant_rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}
    plant_result = generate_lsystem("X", plant_rules, 2)
    print(f"L-System Plant (2 iterations): {plant_result}")
