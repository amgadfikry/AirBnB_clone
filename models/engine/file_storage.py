#!/usr/bin/python3
""" module that steralize and desteralize of instance to json
    and to object """
import json


class FileStorage:
    """ class of file storage that convert object to json
        and convert json to object
        Class Attr:
            file_path: privte attribute to path of json file
            objects: private attribute to stored objects where keys
                are name of class.id of class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ pubic instance method that return all objects of all classes
            Return:
                private class atribute __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ set a new object to __objects class attribute
            Parameters:
                obj: dictionary of new class
        """
        FileStorage.__objects[f"{obj['__class__']}.{obj['id']}"] = obj

    def save(self):
        """ method that steralize __objects attr to json and save it to
            file in _file_path
        """
        with open(FileStorage.__file_path, "w", encoding="utf_8") as fi:
            fi.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """ method desteralize json file to dictionary and save it to
            private attribute __objects
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf_8") as fi:
                reading = fi.read()
                FileStorage.__objects = json.loads(reading)
        except FileNotFoundError:
            pass
