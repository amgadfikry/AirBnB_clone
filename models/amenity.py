#!/usr/bin/python3
""" module that represent amenity model """
from .base_model import BaseModel


class Amenity(BaseModel):
    """ class of amenity model inherit from BaseModel class
        Attr:
            name: public class attr name of amenity
    """
    name = ""
