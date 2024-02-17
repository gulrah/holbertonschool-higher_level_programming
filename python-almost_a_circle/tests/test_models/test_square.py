import unittest
from models.square import Square


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


if __name__ == '__main__':
    unittest.main()
