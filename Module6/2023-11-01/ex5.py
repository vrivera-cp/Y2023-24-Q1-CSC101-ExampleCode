"""ex5.py
An example of unit tests for functions that deal with classes.
"""
import unittest
from vector import Vector
from ex3 import get_magnitude, get_direction


class VectorFunctionTests(unittest.TestCase):

    def test_get_magnitude_01(self):
        x = 3.0
        y = 4.0
        self.assertAlmostEqual(5.0, get_magnitude(x, y))

    def test_get_magnitude_02(self):
        v = Vector(3.0, 4.0)
        self.assertAlmostEqual(5.0, get_magnitude(v.x, v.y))

    def test_get_direction(self):
        v = Vector(-10.0, 10.0)
        self.assertAlmostEqual(135.0, get_direction(v))
