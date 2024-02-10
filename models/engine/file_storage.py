#!/usr/bin/python3
"""
    A custom storage engine for the Air BnB console
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
import json


class FileStorage:
    """
        Simulating a storage system using JSON
    """
    # Class Attributes to ensure global recall.
    __file_path = "./file.json"
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
        for key, val in FileStorage.__objects.items():
            tmp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as db:
            json.dump(tmp, db)

    def reload(self):
        """ Deserialize the json file for information retrieval """
        try:
            with open(FileStorage.__file_path, 'r') as db:
                FileStorage.__objects = json.load(db)
            for key, obj in FileStorage.__objects.items():
                FileStorage.__objects[key] = eval(obj["__class__"])(**obj)
        except Exception:
            pass
