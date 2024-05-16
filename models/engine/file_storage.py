#!/usr/bin/python3
"""
A module defining our file storage object
"""
import json

class FileStorage:
    """
    Our file storage object class definition
    """

    def __init__(self, file_path):
        """
        Initialize a new file storage object
        """
        self.__file_path = file_path
        self.__objects = dict()

    def all(self):
        """
        Returns the dictionary self.__objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Add a new object into the storage
        """
        obj_dict = obj.to_dict()
        self.__objects[obj_dict["__class__"] + "." + obj_dict["id"]] = obj_dict

    def save(self):
        """
        Save the contents of __objects to filepath
        """
        objects_as_json = json.dumps(self.__objects)
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            fp.write(objects_as_json)

    def reload(self):
        """
        Reload the content of the file in file_path
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fp:
                file_content = fp.read()
                self.__objects = json.loads(file_content)
        except FileNotFoundError:
            return
