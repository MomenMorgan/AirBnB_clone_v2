#!/usr/bin/python3
"""test for BaseModel"""
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """testing the base model class"""

    @classmethod
    def setUpClass(cls):
        """prepare for the test"""
        cls.base = BaseModel()
        cls.base.name = "lol"
        cls.base.num = 20

    @classmethod
    def tear_down(cls):
        """tearing down after test"""
        del cls.base

    def tear_Down(self):
        """tearing down after test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def testing_docstring_basemodel(self):
        """checks for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def testing_basemodel_methods(self):
        """testing Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def testing_init(self):
        """testing  the type of BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def testing_save(self):
        """testing or save"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def testing_to_dict_basemodel(self):
        """testing for dictionary"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
