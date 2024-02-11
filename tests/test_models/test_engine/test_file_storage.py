#!/usr/bin/python3
"""
Unittest for the FileStorage system/class
"""
import unittest
from models.engine.file_storage import FileStorage
import models
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

    def test_new(self):
        """ Tests the creation of a new object of any class """
        try:
            models.storage.reload()
            base = BaseModel()
            models.storage.new(base)
            self.assertIn(base, models.storage.all().values())
            person = User()
            models.storage.new(person)
            self.assertIn(person, models.storage.all().values())
            local = State()
            models.storage.new(local)
            self.assertIn(local, models.storage.all().values())
            town = City()
            models.storage.new(town)
            self.assertIn(town, models.storage.all().values())
            item = Amenity()
            models.storage.new(item)
            self.assertIn(item, models.storage.all().values())

            comment = Review()
            models.storage.new(comment)
            self.assertIn(comment, models.storage.all().values())

        except FileNotFoundError:
            models.storage = FileStorage()
            test_new()

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
