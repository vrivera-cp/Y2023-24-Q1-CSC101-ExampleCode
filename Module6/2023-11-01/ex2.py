"""ex2.py
An example of unit tests for __init__, __eq__, __str__, and __repr__.
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

    def test_vector_str(self):
        vector = Vector(1.0, 1.0)
        string = str(vector)

        self.assertEqual('(1.0, 1.0)', string)

    def test_vector_repr(self):
        self.assertEqual('Vector(x=1.0, y=1.0)', repr(Vector(1.0, 1.0)))