#!/usr/bin/python3
"""Unittest for rectangle.py"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def setUp(self):
        """Reset object count before each test."""
        Rectangle._Base__nb_objects = 0

    def test_initialization(self):
        """Test proper initialization of attributes."""
        r = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_width_validation(self):
        """Test width validation."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_height_validation(self):
        """Test height validation."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_validation(self):
        """Test x validation."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "3", 4)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, 4)

    def test_y_validation(self):
        """Test y validation."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -4)

    def test_area(self):
        """Test the area calculation."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        """Test the display of the rectangle."""
        r = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with self.assertLogs() as log:
            with self.assertRaises(AttributeError):
                r.display()
            self.assertEqual(log.output, expected_output)

    def test_str(self):
        """Test the __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test the update method with *args."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 5)
        expected_dict = {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
