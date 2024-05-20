#!/usr/bin/python3
"""
A series of unittests for our file storage class
"""
import unittest
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """
    Our file strorage test class
    """

    def test_all_method(self):
        """
        Tests the all method that returns the whole objects on an empty
        storage instance
        """
        self.assertIsInstance(storage.all(), dict)
        an_obj = BaseModel()
        key = an_obj.__class__.__name__ + "." + an_obj.id
        self.assertNotEqual(storage.all(), {})
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], an_obj)


    def test_save_method(self):
        """
        Tests the save method by checking the json of the object with
        the content of the file
        """
        pass

    def test_non_empty_storage_reload(self):
        """
        For this test i duplicated a non empty json file and instantiated
        a FileStorage object from it
        """


class TestFileStorageOnUser(unittest.TestCase):
    """
    Tests for how the filestorage object handles the user object
    """

    def test_user_in_storage(self):
        """
        Tests if a user is in storage
        """
        usr_1 = User()
        usr_2 = User


if __name__ == "__main__":
    unittest.main()
