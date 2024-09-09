#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def setUp(self):
        """Reset the object count before each test."""
        Square._Base__nb_objects = 0

    def test_initialization(self):
        """Test proper initialization of attributes."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 10)

    def test_size_validation(self):
        """Test size validation (same as width/height validation)."""
        with self.assertRaises(TypeError):
            Square("10")
        with self.assertRaises(ValueError):
            Square(-10)

    def test_x_validation(self):
        """Test x validation."""
        with self.assertRaises(TypeError):
            Square(10, "2")
        with self.assertRaises(ValueError):
            Square(10, -2)

    def test_y_validation(self):
        """Test y validation."""
        with self.assertRaises(TypeError):
            Square(10, 2, "3")
        with self.assertRaises(ValueError):
            Square(10, 2, -3)

    def test_area(self):
        """Test the area calculation."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        """Test the __str__ method."""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_update_args(self):
        """Test the update method with *args."""
        s = Square(5, 2, 3, 10)
        s.update(89, 6, 7, 8)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        s = Square(5, 2, 3, 10)
        s.update(id=89, size=6, x=7, y=8)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s = Square(10, 2, 1, 9)
        expected_dict = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
