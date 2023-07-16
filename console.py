#!/usr/bin/python3
""" entry point module to AirBnB project """
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ class that initate command line interpreter of project
        Attr:
            prompt: first prompt
    """

    prompt = "(hbnb) "

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
            if args[0] not in models.classes.keys():
                print("** class doesn't exist **")
                return False
            elif len(args) == 1:
                print("** instance id is missing **")
                return False
            else:
                all_obj = models.storage.all()
                key = f"{args[0]}.{args[1]}"
                for obj in all_obj.keys():
                    if obj == key:
                        return key
                print("** no instance found **")
                return False

    def do_create(self, arg):
        """create new instance of model, save to json file, print the id of it
        using -> create [model name]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        """
        if not arg:
            print("** class name missing **")
        elif arg not in models.classes.keys():
            print("** class doesn't exist **")
        else:
            new = models.classes[arg]()
            models.storage.save()
            print(new.id)

    def do_all(self, arg):
        """print all string representation of specific model or all models
        using -> all or all [model name]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        """
        if arg and arg not in models.classes.keys():
            print("** class doesn't exist **")
        else:
            li = []
            all_obj = models.storage.all()
            if not arg:
                for key, value in all_obj.items():
                    li.append(value.__str__())
            else:
                for key, value in all_obj.items():
                    if key.startswith(arg):
                        li.append(value.__str__())
            if len(li) > 0:
                print(li)

    def do_show(self, arg):
        """print string representation of instance based on class name and id
        using -> show [class name] [id]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        """
        key = self.check_instance(self, arg)
        if key:
            all_obj = models.storage.all()
            print(all_obj[key])

    def do_destroy(self, arg):
        """delete instance based on class name and id and save to json file
        using -> destroy [class name] [id]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        """
        key = self.check_instance(self, arg)
        if key:
            all_obj = models.storage.all()
            del all_obj[key]
            models.storage.save()

    def do_update(self, arg):
        """update or add only one atrribute for instance based on name & id
        using -> update [class name] [id] [attr name] [attr value]
        model names -> [BaseModel, User, State, City, Amenity, Place, Review]
        unchanged attr -> [id, created_at, updated_at]"""
        key = self.check_instance(self, arg)
        args = arg.split(" ")
        if key:
            if len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return
            else:
                try:
                    all_obj = models.storage.all()
                    obj = all_obj[key]
                    n = args[2]
                    if hasattr(obj, n) and type(getattr(obj, n)) is int:
                        value = int(args[3])
                    elif hasattr(obj, n) and type(getattr(obj, n)) is float:
                        value = float(args[3])
                    else:
                        value = args[3]
                    setattr(obj, n, value)
                    obj.save()
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
