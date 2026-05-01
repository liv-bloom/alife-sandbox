import unittest
from cultural_transmission import simulate_meme_spread

class TestCulturalTransmission(unittest.TestCase):
    def test_meme_spread_saturation(self):
        # We run the simulation with a small population and many generations to ensure it saturates
        history = simulate_meme_spread(population_size=10, generations=50)
        self.assertTrue(len(history) > 0)
        self.assertEqual(history[-1], 10) # Should hit saturation
        self.assertEqual(history[0], 1)

if __name__ == '__main__':
    unittest.main()
