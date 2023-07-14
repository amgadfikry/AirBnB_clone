#!/usr/bin/python3
""" module that test user class model """
import unittest
from models import user
from models.user import User


class TestUser(unittest.TestCase):
    """ class test user class model """

    def test_module_doc(self):
        """ method test if there doc for module """
        doc = len(user.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_class_doc(self):
        """ method test if there is doc for class """
        doc = len(User.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_empty_attribute(self):
        """ method test if has class attributes empty """
        new = User()
        self.assertTrue(hasattr(new, "email"))
        self.assertTrue(len(new.email) == 0)
        self.assertTrue(hasattr(new, "password"))
        self.assertTrue(len(new.password) == 0)
        self.assertTrue(hasattr(new, "first_name"))
        self.assertTrue(len(new.first_name) == 0)
        self.assertTrue(hasattr(new, "last_name"))
        self.assertTrue(len(new.last_name) == 0)

    def test_type_attributes(self):
        """ method test type of value of attributes """
        new = User()
        self.assertIs(type(new.email), str)
        self.assertIs(type(new.password), str)
        self.assertIs(type(new.first_name), str)
        self.assertIs(type(new.last_name), str)

    def test_modify_attributes(self):
        """ method test of modified user """
        new = User()
        new.email = "dr.amgad@yahoo.com"
        new.password = "root"
        new.first_name = "amgad"
        new.last_name = "fikry"
        self.assertEqual(new.email, "dr.amgad@yahoo.com")
        self.assertEqual(new.password, "root")
        self.assertEqual(new.first_name, "amgad")
        self.assertEqual(new.last_name, "fikry")


if __name__ == '__main__':
    unittest.main()
