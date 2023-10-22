#!/usr/bin/python3
"""test for city"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """testing the city class"""

    @classmethod
    def setUpClass(cls):
        """prepare for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tear_down(cls):
        """tearing down after test"""
        del cls.city

    def tear_Down(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def testing_docstring_city(self):
        """checks for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def testing_attributes(self):
        """chekcing if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def testing_subclass_city(self):
        """testing city is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def testing_attribute(self):
        """chekcing for attibutes"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def testing_save_city(self):
        """testing for save"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def testing_to_dict(self):
        """testing for dictionary"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
