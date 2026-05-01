import unittest
from game_of_life import next_generation

class TestGameOfLife(unittest.TestCase):
    def test_block_pattern(self):
        # A 2x2 block is a stable "still life" pattern
        grid = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        new_grid = next_generation(grid)
        self.assertEqual(grid, new_grid)

    def test_blinker_pattern(self):
        # A 3x1 blinker oscillates
        grid1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        grid2 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        new_grid = next_generation(grid1)
        self.assertEqual(new_grid, grid2)
        new_grid_again = next_generation(new_grid)
        self.assertEqual(new_grid_again, grid1)

if __name__ == '__main__':
    unittest.main()
