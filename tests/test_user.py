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


if __name__ == "__main__":
    unittest.main()
