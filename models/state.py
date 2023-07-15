#!/usr/bin/python3
""" module that represent state model """
from .base_model import BaseModel


class State(BaseModel):
    """ class of state model inherit from BaseModel class
        Attr:
            name: public class attr name of state
    """
    name = ""
