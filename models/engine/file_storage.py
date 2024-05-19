#!/usr/bin/python3
"""
A module defining our file storage object
"""
import json


class FileStorage:
    """
    Our file storage object class definition
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        Returns the dictionary self.__objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Add a new object into the storage
        """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
        Save the contents of __objects to filepath
        """
        saved = dict()
        for key, val in self.__objects.items():
            saved[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            json.dump(saved, fp)

    def reload(self):
        """
        Reload the content of the file in file_path
        """
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fp:
                content = fp.read()
                loaded = json.loads(content)
                for key, val in loaded.items():
                    instance = eval(val["__class__"])(**val)
                    self.__objects[key] = instance
        except FileNotFoundError:
            return
