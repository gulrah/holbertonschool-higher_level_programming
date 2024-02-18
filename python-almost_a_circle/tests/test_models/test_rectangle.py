#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""

import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout
import sys


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

    def test_create_with_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_with_id_and_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_create_with_id_width_and_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_create_with_id_width_height_and_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_create_with_id_width_height_x_and_y(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_save_to_file_None(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(None)

    def test_save_to_file_empty_list(self):
        with self.assertRaises(ValueError):
            Rectangle.save_to_file([])

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_load_from_file_when_file_doesnt_exist(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_when_file_exists(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        self.assertEqual(Rectangle.load_from_file(), [r])


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


if __name__ == '__main__':
    unittest.main()
