#!/usr/bin/python3
"""
A series of unittests for our file storage class
"""
import unittest
import json
from models.base_model import BaseModel
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
        empty_storage = FileStorage("empty.json")
        self.assertEqual(empty_storage.all(), {})

    def test_empty_storage_reload(self):
        """
        Test reload method on empty file
        """
        empty_file = "empty.json"
        empty_storage = FileStorage(empty_file)
        empty_storage.reload()
        self.assertEqual(empty_storage.all(), {})

    def test_method_new(self):
        """
        Test the new method that saves a new object to the file
        """
        my_obj = BaseModel()
        my_obj.name = "Sample object"
        new_storage = FileStorage("new.json")
        new_storage.new(my_obj)
        self.maxDiff = None
        c_dct = {"BaseModel.{}".format(my_obj.id): my_obj.to_dict()}
        self.assertEqual(new_storage.all(), c_dct)

    def test_save_method(self):
        """
        Tests the save method by checking the json of the object with
        the content of the file
        """
        my_obj = BaseModel()
        my_obj.name = "Sample object"
        new_storage = FileStorage("new.json")
        new_storage.new(my_obj)
        new_storage.save()
        try:
            with open("new.json", "r", encoding="utf-8") as fp:
                content = fp.read()
                self.assertEqual(json.loads(content), new_storage.all())
        except FileNotFoundError:
            pass

    def test_non_empty_storage_reload(self):
        """
        For this test i duplicated a non empty json file and instantiated
        a FileStorage object from it
        """
        self.maxDiff = None
        os_command = "cat file.json > duplicate.json"
        os.system(os_command)
        duplicate_storage = FileStorage("duplicate.json")
        duplicate_storage.reload()
        self.assertNotEqual(duplicate_storage.all(), {})
        os.system("rm duplicate.json")


class TestFileStorageOnUser(unittest.TestCase):
    """
    Tests for how the filestorage object handles the user object
    """
    pass


if __name__ == "__main__":
    unittest.main()
