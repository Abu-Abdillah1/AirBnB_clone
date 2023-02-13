#!/usr/bin/python3
"""Test Suite for FileStorage in models/file_storage.py"""
import os.path
import unittest

import models
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorageInit(unittest.TestCase):
    """Contains test cases against the FileStorage initialization"""

    def test_file_path_is_a_private_class_attr(self):
        """Checks that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Checks that objects is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """Tests initialization without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """Tests storage created in __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)


class TestStorageMethods(unittest.TestCase):
    """Contains test cases against the methods present in FileStorage"""

    @classmethod
    def setUp(self):
        """Code to execute before testing occurs"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Code to execute after tests are executed"""
        # Remove file.json if it exists
        try:
            os.remove("file.json")
        except IOError:
            pass
        # rename tmp.json from setUp() to file.json
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Tests all() method of the FileStorage class"""
        self.assertTrue(type(models.storage.all()) is dict)

        # What if arg is passed? Ohh! TypeError, do your job!
        with self.assertRaises(TypeError):
            models.storage.all(None)


if __name__ == "__main__":
    unittest.main()
