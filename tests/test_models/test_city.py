#!/usr/bin/python3
"""
unit test for town_storage
"""
import unittest
from models.city import City


class testCity(unittest.TestCase):
    """
        Test the City class
    """
    def test_unique_uuid(self):
        """ Test if the id of town is unique """
        town = City()
        town2 = City()
        self.assertNotEqual(town.id, town2.id)

    def test_attributes(self):
        """ Test if variables can be assigned to class """
        town = City()
        self.assertEqual(town.name, '')
        self.assertEqual(town.state_id, '')
        town.name = "Finland"
        town.state_id = "009-213"
        self.assertEqual(town.name, 'Finland')
        self.assertEqual(town.state_id, '009-213')
        town2 = City()
        self.assertNotEqual(town.name, town2.name)
        self.assertNotEqual(town.state_id, town2.state_id)
        self.assertEqual(town2.name, '')
        self.assertEqual(town2.state_id, '')

    def test_idType(self):
        """
        test if id a string
        """
        town = City()
        self.assertEqual(str, type(town.id))

    def test_save(self):
        """ Test the idType of the class """
        town = City()
        self.assertEqual(str, type(town.id))

    def test_save(self):
        """ Test the save method """
        town = City()
        oldtime = town.updated_at
        town.save()
        self.assertNotEqual(town.updated_at, oldtime)

    def test_save_created_at(self):
        """ Check if class attribute is constant """
        town = City()
        old_created_at = town.created_at
        town.save()
        self.assertEqual(town.created_at, old_created_at)

    def test_updated_at(self):
        """ Tests if save-time updates """
        town = City()
        town.save()
        self.assertNotEqual(town.created_at, town.updated_at)

    def test_display(self):
        """ Test the display of the class """
        town = City()
        disp = f"[City] ({town.id}) {town.__dict__}"
        self.assertEqual(disp, town.__str__())

    def test_dict(self):
        """ Test the dictionary public method """
        town = City()
        self.assertIn('__class__', town.to_dict())
        self.assertIn('created_at', town.to_dict())
        self.assertIn('updated_at', town.to_dict())
