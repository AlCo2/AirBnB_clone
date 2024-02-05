#!/usr/bin/python3
"""
BaseModel class that defines all
common attributes/methodes for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model class definition
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        newdict = self.__dict__.copy()
        newdict['created_at'] = self.created_at.isoformat()
        newdict['updated_at'] = self.updated_at.isoformat()
        return newdict

    def __str__(self):
        reprstr = '[' + str(type(self).__name__) + '] '
        reprstr += '(' + self.id + ') ' + str(self.__dict__)
        return reprstr
