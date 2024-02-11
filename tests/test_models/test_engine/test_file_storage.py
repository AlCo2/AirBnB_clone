#!/usr/bin/python3
"""
Unittest for the FileStorage system/class
"""
import unittest
from models.engine.file_storage import FileStorage
import models
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """ Test the File Storage system """

    def setUp(self):
        """ set up teest env """
        models.storage = FileStorage()

    def tearDown(self):
        """ clean files created """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_new(self):
        """ Tests the creation of a new object of any class """
        models.storage.reload()
        base = BaseModel()
        models.storage.new(base)
        self.assertIn(base, models.storage.all().values())

    def test_save(self):
        """ Tests the serialization of the class """
        models.storage.save()
        with open("file.json", 'r') as db:
            content = db.read()
            self.assertIs(type(content), str)
            self.assertIs(type(json.loads(content)), dict)

    def test_reload_all(self):
        """ Tests the deserialization of class objects """
        try:
            models.storage.reload()
            r_storage = models.storage.all()
            for obj in r_storage.values():
                self.assertIn(type(obj), [BaseModel, User, State, City,
                                          Amenity, Place, Review])
        except Exception:
            pass

    def test_all(self):
        """ Test the all method """
        self.assertIs(type(models.storage.all()), dict)
        if models.storage.all() != {}:
            for obj in models.storage.all().values():
                self.assertIn(type(obj), [BaseModel, User, State, City,
                                          Amenity, Place, Review])

    def test_reload_empty_file(self):
        """
        test reload when file is empty
        """
        try:
            models.storage.reload()
            self.assertEqual(models.storage.all(), {})
        except Exception:
            pass

    def test_alltype(self):
        """
        test tyoe of storage.all return
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_new_with_args(self):
        """ test add args to new """
        with self.assertRaises(TypeError):
            models.storage.new(User(), 1)

    def test_reload_with_args(self):
        """ add args to reload """
        with self.assertRaises(TypeError):
            models.storage.reload(1)
