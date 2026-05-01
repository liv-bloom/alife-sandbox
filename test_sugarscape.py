import unittest
from sugarscape import Sugarscape

class TestSugarscape(unittest.TestCase):
    def test_initialization(self):
        env = Sugarscape(size=10, num_agents=5)
        self.assertEqual(len(env.agents), 5)
        self.assertEqual(len(env.grid), 10)
        self.assertEqual(len(env.grid[0]), 10)

    def test_step_execution(self):
        env = Sugarscape(size=10, num_agents=5)
        stats_before = env.get_stats()
        
        # Run one step
        env.step()
        
        stats_after = env.get_stats()
        # Ensure it doesn't crash and stats are returned
        self.assertTrue("alive" in stats_after)
        self.assertTrue("avg_sugar" in stats_after)

if __name__ == "__main__":
    unittest.main()
