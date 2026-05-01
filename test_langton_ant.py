import unittest
from langton_ant import simulate_ant

class TestLangtonAnt(unittest.TestCase):
    def test_zero_steps(self):
        grid = simulate_ant(0, grid_size=3)
        # Grid should be all 0s
        for row in grid:
            for cell in row:
                self.assertEqual(cell, 0)
                
    def test_one_step(self):
        grid = simulate_ant(1, grid_size=3)
        # Center cell (1, 1) should be 1 (flipped)
        self.assertEqual(grid[1][1], 1)
        # The ant moved to the right (2, 1) but hasn't flipped it yet
        self.assertEqual(grid[1][2], 0)
        # Total active cells should be exactly 1
        total_active = sum(sum(row) for row in grid)
        self.assertEqual(total_active, 1)

    def test_wrap_around(self):
        # Grid size 3, start at 1,1
        # Step 1: dir=0->1 (right), x=2, y=1. grid[1][1]=1
        # Step 2: at 2,1 (white). dir=1->2 (down), x=2, y=2. grid[1][2]=1
        # Step 3: at 2,2 (white). dir=2->3 (left), x=1, y=2. grid[2][2]=1
        # Step 4: at 1,2 (white). dir=3->0 (up), x=1, y=1. grid[2][1]=1
        # Step 5: at 1,1 (black). dir=0->3 (left), x=0, y=1. grid[1][1]=0
        grid = simulate_ant(5, grid_size=3)
        self.assertEqual(grid[1][1], 0) # Center should flip back
        self.assertEqual(grid[1][2], 1)
        self.assertEqual(grid[2][2], 1)
        self.assertEqual(grid[2][1], 1)

if __name__ == '__main__':
    unittest.main()
