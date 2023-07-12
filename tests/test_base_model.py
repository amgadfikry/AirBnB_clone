#!/usr/bin/python3
""" unittest module of base_module class """
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ test case class base model """

    def setUp(self):
        """ method that start with each test """
        self.one = BaseModel()
        self.one.name = "one"
        self.one.age = 15
        self.two = BaseModel()
        self.two.name = "two"
        self.two.age = 20

    def tearDown(self):
        """ method that start with end of each test """
        del self.one
        del self.two

    def test_intsance(self):
        """ method that test if is instance of basemodel """
        self.assertIsInstance(self.one, BaseModel)
        self.assertIsInstance(self.two, BaseModel)

    def test_equality(self):
        """ method that test of equality of two instance  and their id """
        self.assertIsNot(self.one, self.two)
        self.assertNotEqual(self.one, self.two)

    def test_instance_from_dict(self):
        """ method that test create instance from object you created before """
        self.one.save()
        dict_one = self.one.to_dict()
        new = BaseModel(**dict_one)
        self.assertEqual(self.one.id, new.id)
        self.assertEqual(self.one.name, new.name)
        self.assertIsNot(self.one, new)
        type_str = str(type(new.created_at))
        self.assertEqual(type_str, "<class 'datetime.datetime'>")
        self.assertEqual(self.one.created_at, new.created_at)
        self.assertEqual(self.one.updated_at, new.updated_at)
        self.assertEqual(new.to_dict(), dict_one)


if __name__ == '__main__':
    unittest.main()
