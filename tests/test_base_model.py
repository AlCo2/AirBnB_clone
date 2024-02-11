#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):
    """
    working on test cases for BaseModel
    """
    def test_unique_uuid(self):
        """ Test if the id of base is unique """
        base = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base.id, base2.id)

    def test_name(self):
        """ Test if variables can be assigned to class """
        base = BaseModel()
        base.name = "test_name"
        self.assertEqual(base.name, "test_name")

    def test_idType(self):
        """ Test the idType of the class """
        base = BaseModel()
        self.assertEqual(str, type(base.id))

    def test_save(self):
        """ Test the save method """
        base = BaseModel()
        oldtime = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, oldtime)

    def test_save_created_at(self):
        """ Check if class attribute is constant """
        base = BaseModel()
        old_created_at = base.created_at
        base.save()
        self.assertEqual(base.created_at, old_created_at)

    def test_updated_at(self):
        """ Tests if save-time updates """
        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_display(self):
        """ Test the display of the class """
        base = BaseModel()
        disp = f"[BaseModel] ({base.id}) {base.__dict__}"
        self.assertEqual(disp, base.__str__())

    def test_dict(self):
        """ Test the dictionary public method """
        base = BaseModel()
        self.assertIn('__class__', base.to_dict())
        self.assertIn('created_at', base.to_dict())
        self.assertIn('updated_at', base.to_dict())
