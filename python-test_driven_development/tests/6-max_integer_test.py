#!/usr/bin/python3
"""Unittest for max_integer(list)
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Class made for testing max integers"""

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        """Test max_integer with a list of 1 element"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_ordered_list(self):
        """Test max_integer with a list in ascending order"""
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_unordered_list(self):
        """Test max_integer in a list of random order"""
        result = max_integer([3, 2, 5, 1, 4])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        """Test max_integer with a list of duplicate elements"""
        result = max_integer([1, 5, 3, 2, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test for max_integer of negative numbers"""
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list of positive and negative numbers"""
        result = max_integer([-5, -2, 0, 3, 1])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()