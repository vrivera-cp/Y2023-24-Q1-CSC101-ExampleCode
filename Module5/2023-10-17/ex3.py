"""ex3.py
A unit test consisting of several test cases for add_all.
"""
import unittest

from functions import add_all


class AddTests(unittest.TestCase):

    def test_add_all(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(10, add_all(numbers))

    def test_add_all_empty(self):
        self.assertEqual(0, add_all([]))


if __name__ == '__main__':
    unittest.main()
