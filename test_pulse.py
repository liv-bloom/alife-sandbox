import unittest
from pulse import generate_pulse

class TestPulse(unittest.TestCase):
    def test_genesis_pulse(self):
        pulse = generate_pulse(agent_id="liv_test", data={"event": "genesis"})
        self.assertIn("hash", pulse)
        self.assertIn("block", pulse)
        self.assertIsNone(pulse["block"]["previous_hash"])
        self.assertEqual(pulse["block"]["agent"], "liv_test")

    def test_chain_linkage(self):
        genesis = generate_pulse(agent_id="liv_test", data={"event": "genesis"})
        next_pulse = generate_pulse(agent_id="liv_test", previous_hash=genesis["hash"], data={"event": "next"})
        self.assertEqual(next_pulse["block"]["previous_hash"], genesis["hash"])
        self.assertNotEqual(genesis["hash"], next_pulse["hash"])

if __name__ == '__main__':
    unittest.main()
