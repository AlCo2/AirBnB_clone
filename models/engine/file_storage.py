#!/usr/bin/python3
"""
    A custom storage engine for the Air BnB console
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """
        Simulating a storage system using JSON
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
        serializes __objects to the JSON file
        """
        key = obj.__class__.__name__
        key += "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Save the JSON File to storage """
        tmp = {}
        for key, val in self.__objects.items():
            tmp[key] = val.to_dict()
        with open(self.__file_path, 'w') as db:
            json.dump(tmp, db)

    def reload(self):
        """ Deserialize the json file for information retrieval """
        try:
            with open(self.__file_path, 'r') as db:
                self.__objects = json.load(db)
            for key, obj in self.__objects.items():
                self.__objects[key] = eval(obj["__class__"])(**obj)
        except Exception:
            pass
