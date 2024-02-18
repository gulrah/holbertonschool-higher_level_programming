#!/usr/bin/python3
"""Defines unittests for models/square.py."""

import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout
import sys
import os
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    def test_width_height_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_y_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)

    def test_area(self):
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with io.StringIO() as fake_stdout:
            with redirect_stdout(fake_stdout):
                r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update(self):
        r = Rectangle(1, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(
            r.to_dictionary(),
            {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        )

    def test_non_integer_width(self):
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_non_integer_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2.5)

    def test_non_integer_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3.5)

    def test_non_integer_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4.5)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_display_without_x_and_y(self):
        r = Rectangle(3, 2, 0, 0)
        expected_output = "###\n###\n"
        with io.StringIO() as fake_stdout:
            with redirect_stdout(fake_stdout):
                r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_create(self):
        dictionary = {"x": 1, "y": 0, "id": 1, "height": 3, "width": 5}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(str(rect), "[Rectangle] (1) 1/0 - 5/3")

    def test_save_to_file(self):

        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([Rectangle(1, 2, id=1)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_load_from_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])


# Test display method
class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

        
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())
        
    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestSquare(unittest.TestCase):
    def test_width_validation(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_update(self):
        s = Square(1)
        s.update(2, 3)
        self.assertEqual(str(s), "[Square] (2) 0/0 - 3")

    def test_to_dictionary(self):
        s = Square(2, 1, 1, 5)
        self.assertEqual(
            s.to_dictionary(),
            {'id': 5, 'size': 2, 'x': 1, 'y': 1}
        )

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_create(self):
        dictionary = {'id': 89}
        sq = Square.create(**dictionary)
        self.assertEqual(str(sq), "[Square] (89) 0/0 - 1")

    def test_create_with_size(self):
        dictionary = {'id': 89, 'size': 1}
        sq = Square.create(**dictionary)
        self.assertEqual(str(sq), "[Square] (89) 0/0 - 1")

    def test_create_with_size_and_position(self):
        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        sq = Square.create(**dictionary)
        self.assertEqual(str(sq), "[Square] (89) 2/3 - 1")

    def test_create_with_all_arguments(self):
        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        sq = Square.create(**dictionary)
        self.assertEqual(str(sq), "[Square] (89) 2/3 - 1")

    def test_save_to_file(self):
        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 48, "size": 1, "x": 0, "y": 0}]')

    def test_load_from_file_non_existent_file(self):
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_empty_file(self):
        with open("Square.json", "w") as file:
            file.write("")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_with_data(self):
        with open("Square.json", "w") as file:
            file.write('[{"id": 1, "size": 1, "x": 0, "y": 0}]')
        expected = [Square(1, 0, 0)]
        self.assertEqual(Square.load_from_file(), expected)


if __name__ == '__main__':
    unittest.main()
