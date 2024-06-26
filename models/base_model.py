#!/usr/bin/python3

"""
A module that creates the base model for all our objects in the Airbnb project
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Our base model class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of our class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key == "__class__":
                    continue
                self.__setattr__(key, value)
        else:
            self.id = str(uuid4())
            now = datetime.utcnow()
            self.created_at = now
            self.updated_at = now
            storage.new(self)

    def __str__(self):
        """
        Return a string version of the object
        """
        mod_nm = self.__class__.__name__
        mod_id = self.id
        mod_dct = self.__dict__
        return ("[{}] ({}) {}".format(mod_nm, mod_id, mod_dct))

    def save(self):
        """
        This is the save method that currently updates the update_at time only
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        A method that returns the dictionary form of our object
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return (my_dict)
