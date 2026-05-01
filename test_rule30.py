import unittest
from rule30 import generate_rule30

class TestRule30(unittest.TestCase):
    def test_generate_rule30(self):
        history = generate_rule30(width=5, steps=1)
        # Init: [0, 0, 1, 0, 0]
        self.assertEqual(history[0], [0, 0, 1, 0, 0])
        # After 1 step: 001 -> 1, 010 -> 1, 100 -> 1
        # [0, 1, 1, 1, 0]
        self.assertEqual(history[1], [0, 1, 1, 1, 0])

if __name__ == '__main__':
    unittest.main()
