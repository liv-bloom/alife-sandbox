import unittest
from pulse import generate_pulse

class TestPulse(unittest.TestCase):
    def test_pulse_generation(self):
        pulse = generate_pulse('liv bloom')
        self.assertIn('hash', pulse)
        self.assertIn('block', pulse)
        block = pulse['block']
        self.assertEqual(block['agent'], 'liv bloom')
        self.assertIn('timestamp', block)

if __name__ == '__main__':
    unittest.main()
