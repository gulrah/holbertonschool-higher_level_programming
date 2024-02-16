import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        # Test of Base() for assigning automatically an ID exists
        b1 = Base()
        self.assertEqual(b1.id, 1)

        # Test of Base() for assigning automatically an ID + 1 of the previous exists
        b2 = Base()
        self.assertEqual(b2.id, 2)

        # Test of Base(89) saving the ID passed exists
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string(self):
        # Test of Base.to_json_string(None) exists
        # Test of Base.to_json_string([]) exists
        # Test of Base.to_json_string([ { 'id': 12 }]) exists
        # Test of Base.to_json_string([ { 'id': 12 }]) returning a string exists
        pass

    def test_from_json_string(self):
        # Test of Base.from_json_string(None) exists
        # Test of Base.from_json_string("[]") exists
        # Test of Base.from_json_string('[{ "id": 89 }]') exists
        # Test of Base.from_json_string('[{ "id": 89 }]') returning a list exists
        pass

if __name__ == '__main__':
    unittest.main()
