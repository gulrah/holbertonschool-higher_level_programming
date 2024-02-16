import unittest
from models.base import Base, Rectangle, Square


class TestBase(unittest.TestCase):
    def test_auto_assign_id(self):
        # Test Base() for assigning automatically an ID exists
        pass

    def test_auto_assign_id_plus_one(self):
        # Test Base() for assigning automatically an ID + 1 of the previous exists
        pass

    def test_save_passed_id(self):
        # Test Base(89) saving the ID passed exists
        pass

    def test_to_json_string_none(self):
        # Test Base.to_json_string(None) exists
        pass

    def test_to_json_string_empty_list(self):
        # Test Base.to_json_string([]) exists
        pass

    def test_to_json_string_single_dict(self):
        # Test Base.to_json_string([ { 'id': 12 }]) exists
        pass

    def test_to_json_string_returns_string(self):
        # Test Base.to_json_string([ { 'id': 12 }]) returning a string exists
        pass

    def test_from_json_string_none(self):
        # Test Base.from_json_string(None) exists
        pass

    def test_from_json_string_empty_list(self):
        # Test Base.from_json_string("[]") exists
        pass

    def test_from_json_string_single_dict(self):
        # Test Base.from_json_string('[{ "id": 89 }]') exists
        pass

    def test_from_json_string_returns_list(self):
        # Test Base.from_json_string('[{ "id": 89 }]') returning a list exists
        pass


class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        # Test Rectangle(1, 2) exists
        pass

    def test_rectangle_creation_with_x_and_y(self):
        # Test Rectangle(1, 2, 3) exists
        pass

    # Add more test methods for Rectangle with different combinations of arguments


class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        # Test Square(1) exists
        pass

    def test_square_creation_with_x_and_y(self):
        # Test Square(1, 2) exists
        pass

    # Add more test methods for Square with different combinations of arguments


if __name__ == '__main__':
    unittest.main()
