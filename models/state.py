#!/usr/bin/python3
"""
Module Defining an object
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Definition of a State object that inherits from a BaseModel class
    """

    name = ""

    def __init__(self, **kwargs):
        """
        initialize the User object
        """
        super().__init__(**kwargs)
