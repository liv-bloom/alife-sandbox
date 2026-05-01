import unittest
import numpy as np
from reaction_diffusion import ReactionDiffusion

class TestReactionDiffusion(unittest.TestCase):
    def test_initialization(self):
        rd = ReactionDiffusion(size=20)
        self.assertEqual(rd.A.shape, (20, 20))
        self.assertEqual(rd.B.shape, (20, 20))
        # B should be localized in the center
        self.assertEqual(np.sum(rd.B), 100) # 10x10 block in center

    def test_step_execution(self):
        rd = ReactionDiffusion(size=20)
        initial_B_sum = np.sum(rd.B)
        rd.step()
        # Ensure the state has changed after one step
        self.assertNotEqual(np.sum(rd.B), initial_B_sum)
        # Values should remain bounded
        self.assertTrue(np.all((rd.A >= 0) & (rd.A <= 1.0)))
        self.assertTrue(np.all((rd.B >= 0) & (rd.B <= 1.0)))

if __name__ == '__main__':
    unittest.main()
