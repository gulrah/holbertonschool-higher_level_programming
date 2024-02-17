import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create_instance(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_create_instance_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_create_instance_with_negative_id(self):
        with self.assertRaises(ValueError):
            b = Base(-1)


if __name__ == '__main__':
    unittest.main()
