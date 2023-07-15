#!/usr/bin/python3
""" base class module that all classes inherit from it """
import uuid
import datetime
import models


class BaseModel:
    """ base_model class that define all common attributes and methods
        for others classes
    """

    def __init__(self, *args, **kwargs):
        """ init magic method that initalize public attributes
            Parameters:
                args: tuples of arguments
                kwargs: dictionary of arguments
            Attr:
                id: unique id by uuid4
                created_id: created datetime
                updated_at: updated datetime
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self.to_dict())

    def __str__(self):
        """ magic method that print string that represent of class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ public instance method that update datetime for
            updated_at attributes
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self.to_dict())
        models.storage.save()

    def to_dict(self):
        """ public instance method that return dictionary contain
            all key/values of __dict__ of instance
        """
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        return new_dict
