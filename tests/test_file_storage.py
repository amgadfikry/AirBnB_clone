#!/usr/bin/python3
""" unittest module to test file storage module with base_model module """
import unittest
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """ class inherit from unittest to test file storage module """

    def setUp(self):
        """ method that initiate at first of each test """
        self.new = BaseModel()
        self.new.name = "one"
        self.new.age = 10
        self.new.save()

    def tearDown(self):
        """ method that intiate at end of each test """
        del self.new

    def test_check_save(self):
        """ check save of 'new' instance of base model """
        all_obj = storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new.to_dict())

    def test_new_instance(self):
        """ check new instance in storage """
        new2 = BaseModel()
        all_obj = storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new.to_dict())
        new_obj = all_obj[f"BaseModel.{new2.id}"]
        self.assertEqual(new_obj, new2.to_dict())


if __name__ == '__main__':
    unittest.main()
