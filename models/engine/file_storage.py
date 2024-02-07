#!/usr/bin/python3
"""
File to represnet FileStorage class
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    sFileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances
    """

    def __init__(self):
        """
        init method of filestorage
        """
        self.__file_path = "file.json"
        self.__objects = {}

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
        """
        serializes __objects to the JSON file
        """
        objectscpy = {}
        for key, obj in self.__objects.items():
            objectscpy[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(objectscpy))

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    for key, value in json.load(file).items():
                        self.__objects[key] = eval(value["__class__"])(**value)
                except:
                    pass
