#!/usr/bin/python3
"""
Test module for the class User from the module user
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    unit tests for the functionalities provided by the
    User class
    """

    def setUp(self):
        """
        set up a User object for our tests
        """
        self.plc = Place()

    def test_issubclass_of(self):
        """
        Tests if the user class is a subclass of the BaseModel
        class
        """
        self.assertIsInstance(self.plc, BaseModel)
        self.assertTrue(issubclass(self.plc.__class__, BaseModel))

    def test_public_attributes_types(self):
        """
        tests the types of the public user attributes
        """
        self.assertIsInstance(self.plc.city_id, str)
        self.assertIsInstance(self.plc.user_id, str)
        self.assertIsInstance(self.plc.name, str)
        self.assertIsInstance(self.plc.description, str)
        self.assertIsInstance(self.plc.number_rooms, int)
        self.assertIsInstance(self.plc.number_bathrooms, int)
        self.assertIsInstance(self.plc.max_guest, int)
        self.assertIsInstance(self.plc.price_by_night, int)
        self.assertIsInstance(self.plc.latitude, float)
        self.assertIsInstance(self.plc.longitude, float)
        self.assertIsInstance(self.plc.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
