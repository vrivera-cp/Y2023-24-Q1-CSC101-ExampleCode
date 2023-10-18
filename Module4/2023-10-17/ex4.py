"""ex4.py
A unit test consisting of several test cases for repeat.
"""
import unittest

from functions import repeat


class RepeatTests(unittest.TestCase):

    def test_repeat_int(self):
        expected = [2, 2, 2, 2]
        self.assertListEqual(expected, repeat(2, 4))  # same as self.assertEqual()

    def test_repeat_zero(self):
        self.assertEqual([], repeat(False, 0))

    def test_repeat_str(self):
        expected = [
            'mochi',
            'mochi',
            'mochi',
            'mochi',
            'mochi',
            'mochi',
        ]

        self.assertEqual(expected, repeat('mochi', 6))


if __name__ == '__main__':
    unittest.main()
