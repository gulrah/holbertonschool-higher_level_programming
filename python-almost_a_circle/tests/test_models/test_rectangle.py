import unittest
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout
import os
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_width_height_validation(self, mock_stdout):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_x_y_validation(self, mock_stdout):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_area(self, mock_stdout):
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with redirect_stdout(mock_stdout):
            r.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update(self, mock_stdout):
        r = Rectangle(1, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_to_dictionary(self, mock_stdout):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(
            r.to_dictionary(),
            {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        )

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_non_integer_width(self, mock_stdout):
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_non_integer_height(self, mock_stdout):
        with self.assertRaises(TypeError):
            Rectangle(1, 2.5)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_non_integer_x(self, mock_stdout):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3.5)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_non_integer_y(self, mock_stdout):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4.5)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_width(self, mock_stdout):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_height(self, mock_stdout):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zero_width(self, mock_stdout):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zero_height(self, mock_stdout):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_x(self, mock_stdout):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_y(self, mock_stdout):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_without_x_and_y(self, mock_stdout):
        r = Rectangle(3, 2, 0, 0)
        expected_output = "###\n###\n"
        with redirect_stdout(mock_stdout):
            r.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create(self, mock_stdout):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/2")
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/0 - 1/2")
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_save_to_file(self, mock_stdout):
        filename = "test_rectangle.json"
        Rectangle.save_to_file(None)
        self.assertFalse(os.path.exists(filename))
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_load_from_file(self, mock_stdout):
        filename = "test_rectangle.json"
        # Test when file doesn't exist
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])
        # Test when file exists
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)
        self.assertEqual(rectangles[0].to_dictionary(), r.to_dictionary())
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
