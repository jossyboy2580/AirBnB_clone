#!/usr/bin/python3
"""
Test module for the class User from the module user
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    unit tests for the functionalities provided by the
    User class
    """

    def setUp(self):
        """
        set up a User object for our tests
        """
        self.usr = User()

    def test_issubclass_of(self):
        """
        Tests if the user class is a subclass of the BaseModel
        class
        """
        self.assertIsInstance(self.usr, BaseModel)
        self.assertTrue(issubclass(self.usr.__class__, BaseModel))

    def test_public_attributes_types(self):
        """
        tests the types of the public user attributes
        """
        self.assertIsInstance(self.usr.email, str)
        self.assertIsInstance(self.usr.password, str)
        self.assertIsInstance(self.usr.first_name, str)
        self.assertIsInstance(self.usr.last_name, str)


if __name__ == "__main__":
    unittest.main()
