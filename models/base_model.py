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
    def __init__(self, *args, **kwargs):
        """
        init the class BaseModel
        """
        if kwargs:
            for key in kwargs:
                if key == '__class__':
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(kwargs[key],
                            '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
        updates the public instance attr updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        return a dict containing all keys/values
        of __dict__
        """
        newdict = self.__dict__.copy()
        newdict['created_at'] = self.created_at.isoformat()
        newdict['updated_at'] = self.updated_at.isoformat()
        newdict['__class__'] = type(self).__name__
        return newdict

    def __str__(self):
        """
        print [<class name>] (<self.id>) <self.__dict__>
        """
        reprstr = '[' + str(type(self).__name__) + '] '
        reprstr += '(' + self.id + ') ' + str(self.__dict__)
        return reprstr
