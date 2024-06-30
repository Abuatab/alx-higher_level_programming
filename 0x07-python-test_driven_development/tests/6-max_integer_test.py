# !/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max(unittest.TestCase):
    def test_max_integer(self):
        """Unittest for max_integer()"""
        myList = [1, 2, 3, 4]
        self.assertEqual(max_integer(myList), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        myList = [-1, -2, -3, -4]
        self.assertEqual(max_integer(myList), -1)

    def test_mixed_numbers(self):
        myList = [1, -2, 3, 0]
        self.assertEqual(max_integer(myList), 3)
