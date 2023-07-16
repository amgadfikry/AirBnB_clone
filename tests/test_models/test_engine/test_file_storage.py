#!/usr/bin/python3
""" unittest module to test file storage module with base_model module """
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine import file_storage
from models import __init__


class TestFileStorage(unittest.TestCase):
    """ class inherit from unittest to test file storage module """

    def setUp(self):
        """ method that initiate at first of each test """
        self.new = BaseModel()

    def tearDown(self):
        """ method that intiate at end of each test """
        del self.new

    def test_doc_module(self):
        """ method test if there doc for module """
        doc = len(file_storage.__doc__.strip())
        self.assertTrue(doc > 0)
        doc = len(__init__.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_class(self):
        """ method test if there doc for class """
        doc = len(file_storage.FileStorage.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_all_method(self):
        """ method test if there doc for all method """
        doc = len(file_storage.FileStorage.all.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_new_method(self):
        """ method test if there doc for new method """
        doc = len(file_storage.FileStorage.new.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_save_method(self):
        """ method test if there doc for save method """
        doc = len(file_storage.FileStorage.save.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_reload_method(self):
        """ method test if there doc for reload method """
        doc = len(file_storage.FileStorage.reload.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_check_save(self):
        """ check save of 'new' instance of base model """
        all_obj = storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new)

    def test_update_instance_save(self):
        """ method test update instance and save it """
        self.new.name = "new"
        self.new.age = 10
        self.new.save()
        all_obj = storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new)

    def test_new_instance(self):
        """ check new instance in storage """
        new2 = BaseModel()
        all_obj = storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new)
        new_obj = all_obj[f"BaseModel.{new2.id}"]
        self.assertEqual(new_obj, new2)


if __name__ == '__main__':
    unittest.main()
