#!/usr/bin/python3
"""
Module Defining a User object
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Definition of a User object that inherits from a BaseModel class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, **kwargs):
        """
        initialize the User object
        """
        super().__init__(**kwargs)
