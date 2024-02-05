#!/usr/bin/python3
import unittest
from models.base_model import BaseModel 

class testBaseModel(unittest.TestCase):

    def test_unique_uuid(self):
        base = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base.id, base2.id)

    def test_name(self):
        base = BaseModel()
        base.name = "test_name"
        self.assertEqual(base.name, "test_name")
    
    def test_number(self):
        base = BaseModel()
        base.my_number = 89
        self.assertEqual(base.my_number, 89)
