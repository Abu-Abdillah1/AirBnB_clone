#!/usr/bin/python3
"""
This module implements file storage functionalties
"""

import json

from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Srializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        :param obj: obj of type dict
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """

        with open(self.__file_path, "w") as f:
            store = {}
            for k, v in self.__objects.items():
                store[k] = v.to_dict()
            json.dump(store, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists.
        Otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
