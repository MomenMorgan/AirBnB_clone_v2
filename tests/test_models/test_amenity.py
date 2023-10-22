#!/usr/bin/python3
"""test for amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """testing the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """prepare for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "WiFi"

    @classmethod
    def tear_down(cls):
        """tearing down after test"""
        del cls.amenity

    def tear_Down(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def testing_docstring_amenity(self):
        """checks for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def testing_attributes(self):
        """chekcing for attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def testing_subclass_amenity(self):
        """testing if Amenity is a subclass"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def testing_attribute_types(self):
        """testing attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def testing_save(self):
        """testing for save"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def testing_to_dict(self):
        """testing  dictionary """
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()