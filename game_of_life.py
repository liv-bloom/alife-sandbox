# game_of_life.py
# Conway's Game of Life: A classic cellular automaton seed.

def next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            alive_neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        alive_neighbors += grid[nr][nc]
            
            if grid[r][c] == 1:
                if alive_neighbors in [2, 3]:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = 0
            else:
                if alive_neighbors == 3:
                    new_grid[r][c] = 1
                    
    return new_grid

if __name__ == "__main__":
    # Glider pattern
    initial_grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    print("Generation 0:")
    for row in initial_grid: print(row)
    gen1 = next_generation(initial_grid)
    print("Generation 1:")
    for row in gen1: print(row)
