import unittest
import json
from pulse import generate_pulse

class TestPulse(unittest.TestCase):
    def test_pulse_generation(self):
        pulse = generate_pulse('liv bloom')
        self.assertIn('agent_id', pulse)
        self.assertEqual(pulse['agent_id'], 'liv bloom')
        self.assertIn('timestamp', pulse)
        self.assertIn('state_hash', pulse)
        self.assertIn('signature', pulse)

if __name__ == '__main__':
    unittest.main()
