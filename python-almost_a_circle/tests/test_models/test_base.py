import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create_rectangle(self):
        input_dict = {'width': 2, 'height': 3}
        new_rect = Base.create(**input_dict)
        self.assertEqual(new_rect.width, 2)
        self.assertEqual(new_rect.height, 3)

    def test_create_rectangle_with_positional_arguments(self):
        new_rect = Base.create(2, 3)
        self.assertEqual(new_rect.width, 2)
        self.assertEqual(new_rect.height, 3)

    def test_create_rectangle_with_additional_attributes(self):
        input_dict = {'width': 2, 'height': 3, 'x': 12, 'y': 1, 'id': 89}
        new_rect = Base.create(**input_dict)
        self.assertEqual(new_rect.width, 2)
        self.assertEqual(new_rect.height, 3)
        self.assertEqual(new_rect.x, 12)
        self.assertEqual(new_rect.y, 1)
        self.assertEqual(new_rect.id, 89)

    def test_create_square(self):
        input_dict = {'size': 2}
        new_square = Base.create(**input_dict)
        self.assertEqual(new_square.size, 2)

    def test_create_square_with_positional_arguments(self):
        new_square = Base.create(2)
        self.assertEqual(new_square.size, 2)

    def test_create_square_with_additional_attributes(self):
        input_dict = {'size': 2, 'x': 1, 'y': 3, 'id': 89}
        new_square = Base.create(**input_dict)
        self.assertEqual(new_square.size, 2)
        self.assertEqual(new_square.x, 1)
        self.assertEqual(new_square.y, 3)
        self.assertEqual(new_square.id, 89)


if __name__ == '__main__':
    unittest.main()
