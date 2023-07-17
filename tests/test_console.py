#!/usr/bin/python3
""" module to test console """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand as hbnb
import os
import models


class TestConsole(unittest.TestCase):
    """ class to test console """

    @staticmethod
    def res(command):
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd(command)
            text = f.getvalue().replace("\n", "")
        return text

    def setUp(self):
        """ set up with each test"""
        self.user_one = self.res("create User")

    def tearDown(self):
        """ start at end of each test """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create(self):
        """test create command"""
        text = self.res("create")
        self.assertEqual(text, "** class name missing **")
        text = self.res("create user")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("create User")
        self.assertTrue(len(text) > 0)

    def test_show(self):
        """test show command"""
        text = self.res("show")
        self.assertEqual(text, "** class name missing **")
        text = self.res("show hhh")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("show User")
        self.assertEqual(text, "** instance id missing **")
        text = self.res("show User 77777")
        self.assertEqual(text, "** no instance found **")
        text = self.res(f"show User {self.user_one}")
        obj = models.storage.all()
        self.assertEqual(text, obj[f"User.{self.user_one}"].__str__())

    def test_all(self):
        """test all command"""
        text = self.res("all Mymodel")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("all")
        obj = models.storage.all()
        self.assertEqual(text, str([obj[f"User.{self.user_one}"].__str__()]))
        text = self.res("all User")
        self.assertEqual(text, str([obj[f"User.{self.user_one}"].__str__()]))
        text = self.res("all Place")
        self.assertTrue(len(text) == 0)

    def test_destroy(self):
        """test destroy command"""
        text = self.res("destroy")
        self.assertEqual(text, "** class name missing **")
        text = self.res("destroy hhhh")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("destroy User")
        self.assertEqual(text, "** instance id missing **")
        text = self.res("destroy User 77777")
        self.assertEqual(text, "** no instance found **")
        text = self.res(f"destroy User {self.user_one}")
        self.assertEqual(len(text), 0)
        text = self.res(f"show User {self.user_one}")
        self.assertEqual(text, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
