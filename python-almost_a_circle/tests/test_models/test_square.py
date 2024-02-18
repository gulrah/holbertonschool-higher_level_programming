import unittest
import os
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
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), len(expected))
        for loaded_obj, expected_obj in zip(loaded, expected):
            self.assertEqual(loaded_obj.id, expected_obj.id)
            self.assertEqual(loaded_obj.size, expected_obj.size)
            self.assertEqual(loaded_obj.x, expected_obj.x)
            self.assertEqual(loaded_obj.y, expected_obj.y)

if __name__ == '__main__':
    unittest.main()
