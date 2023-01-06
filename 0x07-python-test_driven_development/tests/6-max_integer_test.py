#!/usr/bin/python3
"""import unittest"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """defines test cases for max int"""

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([]), None)
