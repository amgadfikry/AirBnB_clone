#!/usr/bin/python3
""" module that represent city class model """
from .base_model import BaseModel


class City(BaseModel):
    """ class of city model
        Attr:
            state_id: public class attr for State.id
            name: plublic class attr for name of city
    """
    state_id = ""
    name = ""
