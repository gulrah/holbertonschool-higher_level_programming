#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""

import io
import sys
import unittest
import os
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle



import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test calculation of area
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_perimeter(self):
        # Test calculation of perimeter
        r = Rectangle(5, 10)
        self.assertEqual(r.perimeter(), 30)

    def test_scale_size(self):
        # Test scaling size
        r = Rectangle(5, 10)
        r.scale_size(2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)

    def test_width_getter(self):
        # Test width getter
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)

    def test_width_setter(self):
        # Test width setter
        r = Rectangle(5, 10)
        r.width = 15
        self.assertEqual(r.width, 15)

    def test_height_getter(self):
        # Test height getter
        r = Rectangle(5, 10)
        self.assertEqual(r.height, 10)

    def test_height_setter(self):
        # Test height setter
        r = Rectangle(5, 10)
        r.height = 20
        self.assertEqual(r.height, 20)

    def test_str(self):
        # Test string representation
        r = Rectangle(5, 10)
        self.assertEqual(str(r), "Rectangle(5, 10)")

if __name__ == '__main__':
    unittest.main()
