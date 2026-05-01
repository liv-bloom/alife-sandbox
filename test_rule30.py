import unittest
from rule30 import Rule30

class TestRule30(unittest.TestCase):
    def test_initialization(self):
        ca = Rule30(size=21)
        self.assertEqual(len(ca.state), 21)
        self.assertEqual(ca.state[10], 1)
        self.assertEqual(sum(ca.state), 1)

    def test_step(self):
        ca = Rule30(size=21)
        ca.step()
        # After 1 step, the center '1' should expand to '111'
        self.assertEqual(ca.state[9], 1)
        self.assertEqual(ca.state[10], 1)
        self.assertEqual(ca.state[11], 1)

if __name__ == '__main__':
    unittest.main()
