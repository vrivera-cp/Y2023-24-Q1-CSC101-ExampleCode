"""ex1.py
An example of unit tests for __init__ and __eq__.
"""

import unittest
from vector import Vector


class VectorTests(unittest.TestCase):

    def test_vector_init(self):
        vector = Vector(1.0, 2.0)

        self.assertAlmostEqual(vector.x, 1.0)
        self.assertAlmostEqual(vector.y, 2.0)

    def test_vector_eq_01(self):
        a = Vector(1.0, 2.0)
        b = Vector(1.0, 2.0)

        self.assertTrue(a == b)

    def test_vector_eq_02(self):
        a = Vector(0.0, 0.0)
        b = Vector(1.0, 1.0)

        self.assertFalse(a == b)

    def test_vector_eq_03(self):
        a = Vector(0.0, 0.0)

        self.assertFalse(a == ['not', 'a', 'vector'])
