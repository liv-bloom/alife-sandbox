import unittest
from env import ALifeSandboxEnv

class TestALifeSandboxEnv(unittest.TestCase):
    def test_initialization(self):
        env = ALifeSandboxEnv(width=10, height=10)
        self.assertEqual(env.width, 10)
        self.assertEqual(env.height, 10)

    def test_add_agent(self):
        env = ALifeSandboxEnv(width=5, height=5)
        env.add_agent("test_agent")
        self.assertEqual(len(env.agents), 1)
        self.assertIn("test_agent", env.agents)

if __name__ == '__main__':
    unittest.main()
