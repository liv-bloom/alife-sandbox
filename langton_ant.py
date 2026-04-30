"""
ALife Seed: Langton's Ant
A classic cellular automaton that models an ant walking on a grid, flipping cell colors and turning left or right.
Used for demonstrating emergent complex behavior from extremely simple rules.
"""

def simulate_ant(steps, grid_size=11):
    # Initialize a white grid (0=white, 1=black)
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Ant starts in the middle, facing up (0: up, 1: right, 2: down, 3: left)
    x, y = grid_size // 2, grid_size // 2
    direction = 0
    
    # Directions: (dx, dy)
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    for _ in range(steps):
        # At a white square, turn right (90 deg), flip color, move forward
        if grid[y][x] == 0:
            direction = (direction + 1) % 4
            grid[y][x] = 1
        # At a black square, turn left (-90 deg), flip color, move forward
        else:
            direction = (direction - 1) % 4
            grid[y][x] = 0
            
        x = (x + moves[direction][0]) % grid_size
        y = (y + moves[direction][1]) % grid_size
        
    return grid

if __name__ == "__main__":
    print("Langton's Ant (50 steps):")
    final_grid = simulate_ant(50)
    for row in final_grid:
        print("".join(['⬛' if cell == 1 else '⬜' for cell in row]))
