import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_base_automatic_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_automatic_id_increment(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_with_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_base_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_base_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89 }]'), [{'id': 89}])


class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    # Add more test cases for Rectangle methods...


class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    # Add more test cases for Square methods...


if __name__ == '__main__':
    unittest.main()
