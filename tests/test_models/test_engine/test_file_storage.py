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
        bm = None
        with self.assertRaises(TypeError):
            storage.save(bm)
        bm2 = BaseModel()
        bm2_key = "BaseModel.{}".format(bm2.id)
        storage.save()
        file_n = storage.__class__._FileStorage__file_path
        with open(file_n, "r", encoding="utf-8") as fp:
            content = json.load(fp)
            self.assertIn(bm2_key, content.keys())

    def test_non_empty_storage_reload(self):
        """
        For this test i duplicated a non empty json file and instantiated
        a FileStorage object from it
        """
        bm2 = BaseModel()
        bm2_key = "BaseModel.{}".format(bm2.id)
        storage.save()
        storage.reload()
        file_n = storage.__class__._FileStorage__file_path
        with open(file_n, "r", encoding="utf-8") as fp:
            content = json.load(fp)
            self.assertIn(bm2_key, content.keys())

    def test_attribs_not_none(self):
        """
        test that the attributes are not none
        """
        new_storage = FileStorage()
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)


if __name__ == "__main__":
    unittest.main()
