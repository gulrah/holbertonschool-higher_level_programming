#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from models.rectangle import Rectangle
from models.base import Base
from random import randrange
import io
from contextlib import redirect_stdout
import os
from unittest.mock import patch



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
if __name__ == '__main__':
    unittest.main()
