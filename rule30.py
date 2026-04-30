# rule30.py
# 1D Cellular Automaton (Rule 30): An ALife seed demonstrating how complex, 
# pseudo-random patterns can emerge from very simple, deterministic 1D rules.

def generate_rule30(width, steps):
    # Initialize with a single active cell in the center
    state = [0] * width
    state[width // 2] = 1
    
    history = [state]
    
    for _ in range(steps):
        next_state = [0] * width
        for i in range(width):
            left = state[i - 1] if i > 0 else 0
            center = state[i]
            right = state[i + 1] if i < width - 1 else 0
            
            # Rule 30 logic: 111->0, 110->0, 101->0, 100->1, 011->1, 010->1, 001->1, 000->0
            pattern = (left << 2) | (center << 1) | right
            next_state[i] = 1 if pattern in (1, 2, 3, 4) else 0
            
        history.append(next_state)
        state = next_state
        
    return history

def print_history(history):
    for row in history:
        print("".join(["█" if cell else " " for cell in row]))

if __name__ == "__main__":
    width = 31
    steps = 15
    print(f"Generating Rule 30 (width: {width}, steps: {steps}):\n")
    history = generate_rule30(width, steps)
    print_history(history)
