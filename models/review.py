#!/usr/bin/python3
"""
Describes the review system of the console
Allows Users make reviews on Places
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines a review made """
    place_id = ""
    user_id = ""
    text = ""
