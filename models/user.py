#!/usr/bin/python3
""" module that make User class """
from .base_model import BaseModel


class User(BaseModel):
    """class user that inherit from base class
        Attr:
            email: emaul of user
            password: password of user
            first_name: first name of user
            last_name: last name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
