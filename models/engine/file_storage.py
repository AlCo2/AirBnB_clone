#!/usr/bin/python3
"""
    A custom storage engine for the Air BnB console
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
        Simulating a storage system using JSON
    """
    # Class Attributes to ensure global recall.
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """ Returns all saved objects in storage """
        return FileStorage.__objects

    def new(self, obj):
        """ Records the new object in JSON for storage """
        FileStorage.__objects[type(obj).__name__ + "."
                              + obj.id] = obj.to_dict()
        # Should have it assigned to obj. Redo.

    def save(self):
        """ Save the JSON File to storage """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as db:
            json.dump(FileStorage.__objects, db)

    def reload(self):
        """ Deserialize the json file for information retrieval """
        try:
            with open(FileStorage.__file_path, 'r') as db:
                FileStorage. __objects = json.load(db)
        except Exception:
            pass
