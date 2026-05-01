import unittest
from boids import Boid

class TestBoids(unittest.TestCase):
    def test_boid_initialization(self):
        boid = Boid(10, 20)
        self.assertEqual(boid.x, 10)
        self.assertEqual(boid.y, 20)

    def test_boid_update(self):
        boid = Boid(50, 50)
        boid.vx = 1.0
        boid.vy = 0.0
        boid.update()
        self.assertEqual(boid.x, 51.0)
        self.assertEqual(boid.y, 50.0)

if __name__ == '__main__':
    unittest.main()
