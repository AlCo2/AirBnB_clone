#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):
    """
    working on test cases for BaseModel
    """
    def test_unique_uuid(self):
        """
        test if uuid unique
        """
        base = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base.id, base2.id)

    def test_name(self):
        """
        test if name added
        """
        base = BaseModel()
        base.name = "test_name"
        self.assertEqual(base.name, "test_name")

    def test_idType(self):
        """
        test if id a string
        """
        base = BaseModel()
        self.assertEqual(str, type(base.id))

    def test_number(self):
        """
        test using number
        """
        base = BaseModel()
        base.my_number = 89
        self.assertEqual(base.my_number, 89)

    def test_add(self):
        """
        test addition on number
        """
        base = BaseModel()
        base.my_number = 1
        base.my_number += 1
        self.assertEqual(base.my_number, 2)

    def test_save(self):
        """
        test save methode
        """
        base = BaseModel()
        oldtime = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, oldtime)

    def test_save_created_at(self):
        """
        test time change of updated at
        """
        base = BaseModel()
        old_created_at = base.created_at
        base.save()
        self.assertEqual(base.created_at, old_created_at)
