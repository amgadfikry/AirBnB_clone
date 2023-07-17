#!/usr/bin/python3
""" module to test console """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand as hbnb
import os
import models
import console
import cmd


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

    def test_doc(self):
        """test doc of file"""
        text = len(console.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.check_instance.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.do_create.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.do_all.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.do_show.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.do_destroy.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.do_update.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.count.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.split_line.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.default.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.update_multi.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.do_EOF.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.do_quit.__doc__.strip())
        self.assertTrue(text > 0)
        text = len(hbnb.emptyline.__doc__.strip())
        self.assertTrue(text > 0)

    def test_has_attr(self):
        """check if has attr or not"""
        self.assertTrue(hasattr(hbnb, "prompt"))
        self.assertTrue(hasattr(hbnb, "emptyline"))
        self.assertTrue(hasattr(hbnb, "do_quit"))
        self.assertTrue(hasattr(hbnb, "do_EOF"))
        self.assertTrue(hasattr(hbnb, "default"))
        self.assertTrue(hasattr(hbnb, "do_destroy"))
        self.assertTrue(hasattr(hbnb, "count"))
        self.assertTrue(hasattr(hbnb, "split_line"))
        self.assertTrue(hasattr(hbnb, "update_multi"))
        self.assertTrue(hasattr(hbnb, "do_all"))
        self.assertTrue(hasattr(hbnb, "do_show"))
        self.assertTrue(hasattr(hbnb, "do_update"))
        self.assertTrue(hasattr(hbnb, "check_instance"))
        self.assertTrue(hasattr(hbnb, "do_create"))

    def test_prompt_value(self):
        """check prompt value"""
        self.assertEqual(hbnb.prompt, "(hbnb) ")

    def test_instance(self):
        """check instance of hbnb"""
        x = hbnb()
        self.assertTrue(isinstance(x, cmd.Cmd))

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

    def test_class_show(self):
        """test class.show command"""
        text = self.res("hhh.show()")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("User.show()")
        self.assertEqual(text, "** instance id missing **")

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

    def test_class_all(self):
        """test class.all command"""
        text = self.res("Us.all()")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("Place.all()")
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

    def test_class_destroy(self):
        """test class.destroy command"""
        text = self.res("hhh.destroy()")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("User.destroy()")
        self.assertEqual(text, "** instance id missing **")

    def test_count(self):
        """test count command"""
        text = self.res("hh.count()")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("User.count()")
        self.assertTrue(int(text) > 0)

    def test_help(self):
        """test help command"""
        text = self.res("help help")
        self.assertTrue(len(text) > 0)
        text = self.res("help create")
        self.assertTrue(len(text) > 0)
        text = self.res("help show")
        self.assertTrue(len(text) > 0)
        text = self.res("help all")
        self.assertTrue(len(text) > 0)
        text = self.res("help destroy")
        self.assertTrue(len(text) > 0)
        text = self.res("help update")
        self.assertTrue(len(text) > 0)
        text = self.res("help quit")
        self.assertTrue(len(text) > 0)
        text = self.res("help EOF")
        self.assertTrue(len(text) > 0)
        text = self.res("help dd")
        self.assertEqual(text, "*** No help on dd")

    def test_quit(self):
        """test quit command """
        text = self.res("quit")
        self.assertTrue(len(text) == 0)

    def test_update(self):
        """test update command """
        text = self.res("update")
        self.assertEqual(text, "** class name missing **")
        text = self.res("update hhh")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("update User")
        self.assertEqual(text, "** instance id missing **")
        text = self.res("update User 77777")
        self.assertEqual(text, "** no instance found **")
        text = self.res(f"update User {self.user_one}")
        self.assertEqual(text, "** attribute name missing **")
        text = self.res(f"update User {self.user_one} amgad")
        self.assertEqual(text, "** value missing **")
        text = self.res(f"update User {self.user_one} name amgad")
        self.assertEqual(len(text), 0)
        obj = models.storage.all()
        text = self.res(f"show User {self.user_one}")
        self.assertEqual(text, obj[f"User.{self.user_one}"].__str__())
        self.assertEqual(obj[f"User.{self.user_one}"].name, "amgad")

    def test_class_update(self):
        """test class.update"""
        text = self.res("hhh.update()")
        self.assertEqual(text, "** class doesn't exist **")
        text = self.res("User.update()")
        self.assertEqual(text, "** instance id missing **")

    def test_error_code(self):
        """test unknown command"""
        text = self.res("wrong")
        self.assertEqual(text, "*** unknown syntax wrong")


if __name__ == '__main__':
    unittest.main()
