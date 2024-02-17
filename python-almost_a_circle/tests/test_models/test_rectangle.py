import unittest
import io
from unittest import mock
from models.rectangle import Rectangle


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
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
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


if __name__ == '__main__':
    unittest.main()
