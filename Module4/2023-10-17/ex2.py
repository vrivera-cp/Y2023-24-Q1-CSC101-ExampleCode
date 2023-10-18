"""ex2.py
A unit test consisting of single test case for calculate_force.
"""
import unittest

from functions import calculate_force


class MyTests(unittest.TestCase):

    def test_compute_force(self):
        self.assertAlmostEqual(10.0, calculate_force(2.0, 5.0))


if __name__ == '__main__':
    unittest.main()
