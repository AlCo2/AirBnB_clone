#!/usr/bin/python3
"""
Unittest for the FileStorage system/class
"""
import unittest
from models.engine.file_storage import FileStorage
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

    def tearDown(self):
        """ clean files created """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_new(self):
        """ Tests the creation of a new object of any class """

        storage = FileStorage()
        base = BaseModel()
        storage.new(base)
        self.assertIn(base, storage.all().values())

    def test_save(self):
        """ Tests the serialization of the class """
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
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
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        self.assertIs(type(storage.all()), dict)
        if storage.all() != {}:
            for obj in storage.all().values():
                self.assertIn(type(obj), [BaseModel, User, State, City,
                                          Amenity, Place, Review])
