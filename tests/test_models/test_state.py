#!/usr/bin/python3
""" module to test state class """
import unittest
from models import state
from models.state import State


class TestState(unittest.TestCase):
    """ class that test state module and state class """

    def test_module_doc(self):
        """ method test if there doc for module """
        doc = len(state.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_class_doc(self):
        """ method test if there is doc for class """
        doc = len(State.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_empty_attribute(self):
        """ method test if has class attributes empty """
        new = State()
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(len(new.name) == 0)

    def test_type_attributes(self):
        """ method test type of value of attributes """
        new = State()
        self.assertIs(type(new.name), str)

    def test_modify_attributes(self):
        """ method test of modified state """
        new = State()
        new.name = "cairo"
        self.assertEqual(new.name, "cairo")
        self.assertEqual(State.name, "")


if __name__ == '__main__':
    unittest.main()
