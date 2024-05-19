#!/usr/bin/python3
"""
Unittest test cases for our basemodel class
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from io import StringIO
import sys
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    This TestBaseModel class inherits from TestCase
    and it runs tests on the features
    implemented on out base_model module
    """

    def setUp(self):
        """
        A test fixture that sets up the necessary
        objects for out tests
        """
        self.obj = BaseModel()

    def tearDown(self):
        """
        This test fixtur destroys our object
        """
        del self.obj

    def test_base_model_id(self):
        """
        Tests that our base model has an id
        """
        self.assertIsInstance(self.obj.id, str)

    def test_base_model_create_at(self):
        """
        This test checks whether the created_at attribute of our
        class is a datetime object
        """
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_base_model_updated_at(self):
        """
        Test if the updated_at is the same as the created_at when
        our object is instantiated
        """
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertEqual(self.obj.updated_at, self.obj.created_at)

    def test_print_model(self):
        """
        tests if the printed form of the object conforms with the
        required format
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        print(self.obj)
        c_str = '[BaseModel] ({}) {}'.format(self.obj.id, self.obj.__dict__)
        self.assertEqual(captured_output.getvalue().strip(), c_str)
        sys.stdout = sys.__stdout__

    def test_base_model_save(self):
        """
        Tests the instance method save
        """
        before_saving = self.obj.updated_at
        self.obj.save()
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertNotEqual(self.obj.updated_at, before_saving)

    def test_model_to_dict(self):
        """
        Test the to_dict method to confirm we're getting the actual value
        """
        my_dict = dict()
        self.obj.name = "some random name"
        my_dict["name"] = self.obj.name
        my_dict["id"] = str(self.obj.id)
        my_dict["created_at"] = str(self.obj.created_at.isoformat())
        my_dict["updated_at"] = str(self.obj.updated_at.isoformat())
        my_dict["__class__"] = "BaseModel"
        self.assertEqual(my_dict, self.obj.to_dict())

    def test_model_to_dict_types(self):
        """
        Test the types of the values stored in the dictionary
        """
        self.assertIsInstance(self.obj.to_dict()["created_at"], str)

    def test_dict_to_model(self):
        """
        This test will test the use of the dict to instatiate a new model
        """
        my_dict = self.obj.to_dict()
        new_obj = BaseModel(**my_dict)
        self.assertEqual(self.obj.to_dict(), new_obj.to_dict())
        self.assertIsInstance(new_obj, BaseModel)
        self.assertIsInstance(new_obj.created_at, datetime)

    def test_setting_new_obj_in_storage(self):
        """
        This test is to confirm if a new object is entered
        into the storage
        object
        """
        c_key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.assertIn(c_key, storage.all())
