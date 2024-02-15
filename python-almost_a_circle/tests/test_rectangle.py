#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 10)
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -5)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 0, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 0, -5)


if __name__ == '__main__':
    unittest.main()
