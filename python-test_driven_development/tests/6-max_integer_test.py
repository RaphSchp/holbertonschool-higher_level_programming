#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing for a function that returns a max value"""

    def test_max(self):
        """Test for verifying the max value"""
        # test max when in the list 5 is max
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([5, 5, 5, 5, 5]), 5)
        self.assertAlmostEqual(max_integer([5]), 5)
        self.assertAlmostEqual(max_integer([-5]), -5)
        self.assertAlmostEqual(max_integer([-1, -80, -15, -100, -1998000]), -1)
        self.assertAlmostEqual(max_integer([-1, -80, 15, 100, -1998]), 100)

    def test_values(self):
        """Test for assertion raises"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(Exception, max_integer("Hola"))
        self.assertRaises(Exception, max_integer, [4, None, "3"])
        self.assertRaises(Exception, max_integer((4, 5, 6, 7)))
        self.assertRaises(Exception, max_integer, [{4: 2, 2: 1}, (1, 2), 5])
