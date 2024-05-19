#!/usr/bin/python3
"""
Module Defining an object
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Definition of a State object that inherits from a BaseModel class
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, **kwargs):
        """
        initialize the User object
        """
        super().__init__(**kwargs)
