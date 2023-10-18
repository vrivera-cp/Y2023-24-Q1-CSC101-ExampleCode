"""ex6.py
An example of unit tests for functions that deal with classes.
"""
import unittest
from cat_owner import Cat, CatOwner
from cat_functions import owns_cat


class CatOwnerTests(unittest.TestCase):
    def test_owns_cat_01(self):
        cats = [Cat('Harvest', 5), Cat('Pearl', 3)]
        cat_owner = CatOwner('Vanessa', cats)

        requested_cat = Cat('Harvest', 5)

        self.assertTrue(owns_cat(cat_owner, requested_cat))

    def test_owns_cat_02(self):
        cats = [Cat('Harvest', 5), Cat('Pearl', 3)]
        cat_owner = CatOwner('Vanessa', cats)

        requested_cat = Cat('Mochi', 6)

        self.assertFalse(owns_cat(cat_owner, requested_cat))
