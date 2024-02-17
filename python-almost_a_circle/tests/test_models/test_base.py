import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create_instance(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_create_instance_increment_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_create_instance_with_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89 }]'), [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
