import unittest
import json
import os
from pulse import generate_pulse

class TestPulse(unittest.TestCase):
    def test_pulse_generation(self):
        pulse = generate_pulse()
        self.assertIn('agent', pulse)
        self.assertEqual(pulse['agent'], 'liv bloom')
        self.assertIn('timestamp', pulse)
        self.assertIn('state_hash', pulse)
        self.assertIn('signature', pulse)

if __name__ == '__main__':
    unittest.main()
