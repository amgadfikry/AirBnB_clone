#!/usr/bin/python3
""" module that represent place model """
from .base_model import BaseModel


class Place(BaseModel):
    """ class of place model inherit from BaseModel class
        Attr:
            city_id: public class attr id of city
            user_id: public class attr id of user
            name: public class attr name of state
            description: public class attr of description of place
            number_rooms: public class attr of number of rooms
            number_bathrooms: public class attr number of bathroom
            max_guest: public class attr max number of guests
            price_by_night: public class attr price per night
            latitude: public class attr of latitude of place
            longitude: public class attr of longitude of place
            amenity_ids: public class attr of list of amenity of id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
