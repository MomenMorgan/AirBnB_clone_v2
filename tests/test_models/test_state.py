#!/usr/bin/python3
"""test for state"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """testing State class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def tear_down(cls):
        """tearing down after test"""
        del cls.state

    def tear_Down(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def testing_docstring_state(self):
        """checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def testing_attributes(self):
        """chekcing for attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def testing_subclass_state(self):
        """testing State subclass"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def testing_attribute_types(self):
        """testing attribute type"""
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_state(self):
        """testing  save"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_state(self):
        """testing  dictionary"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
