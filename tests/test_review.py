#!/usr/bin/python3
""" module to test review class """
import unittest
from models import review
from models.review import Review


class TestReview(unittest.TestCase):
    """ class that test review module and Review class """

    def test_module_doc(self):
        """ method test if there doc for module """
        doc = len(review.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_class_doc(self):
        """ method test if there is doc for class """
        doc = len(Review.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_empty_attribute(self):
        """ method test if has class attributes empty """
        new = Review()
        self.assertTrue(hasattr(new, "place_id"))
        self.assertTrue(len(new.place_id) == 0)
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(len(new.user_id) == 0)
        self.assertTrue(hasattr(new, "text"))
        self.assertTrue(len(new.text) == 0)

    def test_type_attributes(self):
        """ method test type of value of attributes """
        new = Review()
        self.assertIs(type(new.user_id), str)
        self.assertIs(type(new.place_id), str)
        self.assertIs(type(new.text), str)

    def test_modify_attributes(self):
        """ method test of modified review """
        new = Review()
        new.user_id = "666"
        new.place_id = "555"
        new.text = "text me"
        self.assertEqual(new.text, "text me")
        self.assertEqual(Review.text, "")
        self.assertEqual(new.user_id, "666")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(new.place_id, "555")
        self.assertEqual(Review.place_id, "")


if __name__ == '__main__':
    unittest.main()
