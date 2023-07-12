#!/usr/bin/python3
""" entry point module to AirBnB project """
import cmd


class HBNBCommand(cmd.Cmd):
    """ class that initate command line interpreter of project
        Attr:
            prompt: first prompt
    """

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """EOF handle exit program with 'ctrl + z' or 'ctrl + d'"""
        print()
        return True

    def do_quit(self, arg):
        """quit command is to exit the program"""
        return True

    def emptyline(self):
        """add othing happen when enter empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
