#!/usr/bin/python3
""" module that steralize and desteralize of instance to json
    and to object """
import json
import models


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
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ method that steralize __objects attr to json and save it to
            file in _file_path
        """
        dic = {}
        for key, value in FileStorage.__objects.items():
            dic[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf_8") as fi:
            fi.write(json.dumps(dic))

    def reload(self):
        """ method desteralize json file to dictionary and save it to
            private attribute __objects
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf_8") as fi:
                dic = json.loads(fi.read())
                for key, value in dic.items():
                    obj = models.classes[value["__class__"]](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
