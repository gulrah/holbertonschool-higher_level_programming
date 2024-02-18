#!/usr/bin/python3
"""
Unit Tests for Square class in models.square module
"""

import unittest
import os
from models.square import Square
import sys

class TestSquare(unittest.TestCase):
    def test_positive_dimensions(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_string_arguments(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_to_string_representation(self):
        square = Square(1, id=1)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 1")

    def test_to_dictionary(self):
        square = Square(10, 2, 1, 1)
        self.assertEqual(
            square.to_dictionary(), {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_update_attributes(self):
        square = Square(5)
        square.update(size=7)
        self.assertEqual(square.size, 7)

    def test_create_from_dictionary(self):
        square = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(square.id, 89)
    
    def test_save_to_file(self):
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file([Square(1, id=1)])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "size": 1, "x": 0, "y": 0}]')

    def test_load_from_file(self):
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_constructor_with_two_arguments(self):
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_constructor_with_three_arguments(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_constructor_with_string_argument(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_constructor_with_mixed_type_arguments(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

if __name__ == '__main__':
    unittest.main()
