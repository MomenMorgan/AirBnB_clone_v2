#!/usr/bin/python3
"""
Class for testing the console
"""

import console
import inspect
import pep8
import unittest
HBNBCmd = console.HBNBCommand

class TestingHbnb(unittest.TestCase):
    """testing documentation of the console"""
    def test_pep8_console(self):
        """Testing that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        res = pep8s.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Testing that tests conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        res = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Testing for the console.py docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Testing for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCmd.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCmd.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
