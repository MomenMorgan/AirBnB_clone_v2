#!/usr/bin/python3
"""test for user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """testing the User class"""

    @classmethod
    def setUpClass(cls):
        """prepare for test"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Yook"
        cls.user.email = "yook00627@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def tear_down(cls):
        """tearing down after test"""
        del cls.user

    def tear_Down(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def testing_docstring_user(self):
        """checks for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def testing_attributes_user(self):
        """chekcing for attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def testing_subclass_user(self):
        """testing if User is a subclas"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def testing_attribute_types_user(self):
        """testing attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def testing_save(self):
        """testing save"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def testing_to_dict(self):
        """testing for dictionary"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
