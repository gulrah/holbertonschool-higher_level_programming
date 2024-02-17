#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Set up method to run before each test method.'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Clean up method to run after each test method.'''
        pass

    # Test instantiation of Base class and its attributes
    def test_instantiation(self):
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    # Test consecutive IDs
    def test_consecutive_ids(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    # Test synchronization between class and instance ID
    def test_id_synced(self):
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    # Test custom integer ID
    def test_custom_id_int(self):
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    # Test custom string ID
    def test_custom_id_str(self):
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    # Test passing ID as a keyword argument
    def test_id_keyword_arg(self):
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    # Test to_json_string() method
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        # Add more tests for to_json_string()

    # Test from_json_string() method
    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        # Add more tests for from_json_string()

    # Test save_to_file() method
    def test_save_to_file(self):
        # Add tests for save_to_file() method
        pass

    # Test create() method
    def test_create(self):
        # Add tests for create() method
        pass

    # Test load_from_file() method
    def test_load_from_file(self):
        # Add tests for load_from_file() method
        pass

if __name__ == "__main__":
    unittest.main()
