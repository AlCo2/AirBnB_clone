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

    def test_idType(self):
        base = BaseModel()
        self.assertEqual(str, type(base.id))
    
    def test_number(self):
        base = BaseModel()
        base.my_number = 89
        self.assertEqual(base.my_number, 89)

    def test_add(self):
        base = BaseModel()
        base.my_number = 1
        base.my_number += 1
        self.assertEqual(base.my_number, 2)

    def test_save(self):
        base = BaseModel()
        oldtime = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, oldtime)

    def test_save_created_at(self):
        base = BaseModel()
        old_created_at = base.created_at
        base.save()
        self.assertEqual(base.created_at, old_created_at)
