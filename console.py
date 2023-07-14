#!/usr/bin/python3
""" entry point module to AirBnB project """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ class that initate command line interpreter of project
        Attr:
            prompt: first prompt
    """

    prompt = "(hbnb)"
    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]

    @staticmethod
    def check_instance(self, arg):
        """ static method that check  for availability of instance
            in storage or not and show difrent messages
            Parameters:
                args: arg pass to command
                cmd: type of command
            Return: message if fail or key in objects
        """
        if not arg:
            print("** class name missing **")
            return False
        else:
            args = arg.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return False
            elif len(args) == 1:
                print("** instance id is missing **")
                return False
            else:
                all_obj = storage.all()
                key = f"{args[0]}.{args[1]}"
                for obj in all_obj.keys():
                    if obj == key:
                        temp = obj[:]
                        return temp
                print("** no instance found **")
                return False

    @staticmethod
    def class_from_str(string, **obj):
        """ make class from string
            Parameters:
                string: string of class
                obj: obj to build instance from it
            Return:
                new class
        """
        class_obj = globals()[string.split(".")[0]]
        if len(obj) == 0:
            cls = class_obj()
        else:
            cls = class_obj(**obj)
        return cls

    def do_create(self, arg):
        """create new instance of model, save to json file, print the id of it
        using -> create [model name]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = self.class_from_str(arg)
            storage.save()
            print(new.id)

    def do_all(self, arg):
        """print all string representation of specific model or all models
        using -> all or all [model name]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        """
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
        else:
            li = []
            all_obj = storage.all()
            if not arg:
                for obj in all_obj.keys():
                    cls = self.class_from_str(obj, **all_obj[obj])
                    li.append(cls.__str__())
            elif arg in self.classes:
                for obj in all_obj.keys():
                    if obj.startswith(arg):
                        cls = self.class_from_str(obj, **all_obj[obj])
                        li.append(cls.__str__())
            if len(li) > 0:
                print(li)

    def do_show(self, arg):
        """print string representation of instance based on class name and id
        using -> show [class name] [id]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        """
        obj = self.check_instance(self, arg)
        if obj:
            all_obj = storage.all()
            cls = self.class_from_str(obj, **all_obj[obj])
            print(cls)

    def do_destroy(self, arg):
        """delete instance based on class name and id and save to json file
        using -> destroy [class name] [id]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        """
        obj = self.check_instance(self, arg)
        if obj:
            all_obj = storage.all()
            del all_obj[obj]
            storage.save()

    def do_update(self, arg):
        """update or add only one atrribute for instance based on name & id
        using -> update [class name] [id] [attr name] [attr value]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        unchanged attr -> [id, created_at, updated_at]"""
        obj = self.check_instance(self, arg)
        args = arg.split(" ")
        if obj:
            if len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return
            else:
                try:
                    all_obj = storage.all()
                    cls = self.class_from_str(obj, **all_obj[obj])
                    Class = globals()[args[0]]
                    t = args[2]
                    if hasattr(Class, t) and type(getattr(Class, t)) is int:
                        x = int(args[3])
                    elif hasattr(Class, t) and type(getattr(Class, t)) is float:
                        x = float(args[3])
                    else:
                        x = args[3]
                    setattr(cls, t, x)
                    cls.save()
                except ValueError:
                    pass

    def do_EOF(self, arg):
        """EOF handle exit program with 'ctrl + z' or 'ctrl + d'"""
        print("")
        return True

    def do_quit(self, arg):
        """quit command is to exit the program"""
        return True

    def emptyline(self):
        """add othing happen when enter empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
