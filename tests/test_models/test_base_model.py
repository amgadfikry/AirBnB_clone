#!/usr/bin/python3
""" unittest module of base_module class """
import unittest
import datetime
from models.base_model import BaseModel
import models.base_model


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

    def test_doc_module(self):
        """ method test if there doc for module """
        doc = len(models.base_model.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_class(self):
        """ method test if there doc for class """
        doc = len(BaseModel.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_init_method(self):
        """ method test if there doc for __init__ method """
        doc = len(BaseModel.__init__.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_str_method(self):
        """ method test if there doc for __str__method """
        doc = len(BaseModel.__str__.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_save_method(self):
        """ method test if there doc for save method """
        doc = len(BaseModel.save.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_to_dic_method(self):
        """ method test if there doc for to_dict method """
        doc = len(BaseModel.to_dict.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_intsance(self):
        """ method that test if is instance of basemodel """
        self.assertIsInstance(self.one, BaseModel)
        self.assertIsInstance(self.two, BaseModel)

    def test_equality(self):
        """ method that test of equality of two instance  and their id """
        self.assertIsNot(self.one, self.two)
        self.assertNotEqual(self.one, self.two)

    def test_attributes(self):
        """ method test attributes in instance """
        self.assertEqual(self.one.name, "one")
        self.assertEqual(self.one.age, 15)
        self.assertEqual(self.two.name, "two")
        self.assertEqual(self.two.age, 20)

    def test_different_id(self):
        """ method test if id is equal or not """
        self.assertNotEqual(self.one.id, self.two.id)

    def test_str_method(self):
        """ method test string represtation of class """
        string = f"[BaseModel] ({self.one.id}) {self.one.__dict__}"
        self.assertEqual(self.one.__str__(), string)

    def test_dict_from_instance(self):
        """ method test dict of instance """
        dic = self.one.to_dict()
        self.assertEqual(self.one.id, dic["id"])
        self.assertEqual(self.one.created_at.isoformat(), dic["created_at"])
        self.assertEqual(self.one.updated_at.isoformat(), dic["updated_at"])
        self.assertEqual(self.one.name, dic["name"])
        self.assertEqual(self.one.age, dic["age"])
        self.assertEqual(dic["__class__"], "BaseModel")

    def test_new_instance_from_dict(self):
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
