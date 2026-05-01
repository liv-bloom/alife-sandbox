import unittest
from lsystem import generate_lsystem

class TestLSystem(unittest.TestCase):
    def test_algae(self):
        rules = {"A": "AB", "B": "A"}
        self.assertEqual(generate_lsystem("A", rules, 0), "A")
        self.assertEqual(generate_lsystem("A", rules, 1), "AB")
        self.assertEqual(generate_lsystem("A", rules, 2), "ABA")
        self.assertEqual(generate_lsystem("A", rules, 3), "ABAAB")
        self.assertEqual(generate_lsystem("A", rules, 4), "ABAABABA")
        
    def test_plant(self):
        rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}
        # Iteration 1
        res1 = generate_lsystem("X", rules, 1)
        self.assertEqual(res1, "F+[[X]-X]-F[-FX]+X")
        # Iteration 2 (F becomes FF, X expands)
        res2 = generate_lsystem("X", rules, 2)
        # Expected expansion of 'F'
        self.assertTrue(res2.startswith("FF+"))

if __name__ == '__main__':
    unittest.main()
