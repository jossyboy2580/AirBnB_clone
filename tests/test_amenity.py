#!/usr/bin/python3
"""
Test module for the class User from the module user
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    unit tests for the functionalities provided by the
    User class
    """

    def setUp(self):
        """
        set up a User object for our tests
        """
        self.amn = Amenity()

    def test_issubclass_of(self):
        """
        Tests if the user class is a subclass of the BaseModel
        class
        """
        self.assertIsInstance(self.amn, BaseModel)
        self.assertTrue(issubclass(self.amn.__class__, BaseModel))

    def test_public_attributes_types(self):
        """
        tests the types of the public user attributes
        """
        self.assertIsInstance(self.amn.name, str)


if __name__ == "__main__":
    unittest.main()
