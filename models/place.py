#!/usr/bin/python3
"""
Module Defining an object
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Definition of a Place object that inherits from a BaseModel class
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, **kwargs):
        """
        initialize the User object
        """
        super().__init__(**kwargs)
