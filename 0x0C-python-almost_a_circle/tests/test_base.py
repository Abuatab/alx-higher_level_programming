import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def setUp(self):
        """Set up any state for the tests."""
        Base._Base__nb_objects = 0  # Reset the object count for consistency

    def test_to_json_string(self):
        """Test the to_json_string method."""
        dicts = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        json_string = Base.to_json_string(dicts)
        self.assertEqual(json.loads(json_string), dicts)

        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """Test the from_json_string method."""
        json_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        output = Base.from_json_string(json_string)
        expected = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        self.assertEqual(output, expected)

        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file(self):
        """Test the save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])

        # Check if the file is created and the content matches
        with open("Rectangle.json", "r") as file:
            content = json.load(file)
            expected = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(content, expected)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        os.remove("Rectangle.json")
        os.remove("Square.json")

    def test_load_from_file(self):
        """Test the load_from_file method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])

        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(rectangles[1].to_dictionary(), r2.to_dictionary())

        # Test for empty list when file doesn't exist
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

        os.remove("Rectangle.json")

    def test_create(self):
        """Test the create method."""
        r1_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        r1 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.to_dictionary(), r1_dict)

        s1_dict = {'id': 2, 'size': 5, 'x': 1, 'y': 1}
        s1 = Square.create(**s1_dict)
        self.assertEqual(s1.to_dictionary(), s1_dict)


if __name__ == '__main__':
    unittest.main()
