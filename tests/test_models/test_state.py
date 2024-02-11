#!/usr/bin/python3
"""
unit test for country_storage
"""
import unittest
from models.state import State


class testState(unittest.TestCase):
    """
        Test the State class
    """
    def test_unique_uuid(self):
        """ Test if the id of country is unique """
        country = State()
        country2 = State()
        self.assertNotEqual(country.id, country2.id)

    def test_attributes(self):
        """ Test if variables can be assigned to class """
        country = State()
        self.assertEqual(country.name, '')
        country.name = "Finland"
        self.assertEqual(country.name, 'Finland')
        country2 = State()
        self.assertNotEqual(country.name, country2.name)
        self.assertEqual(country2.name, '')
        country2.name = 'Germany'
        self.assertEqual(country2.name, 'Germany')

    def test_idType(self):
        """
        test if id a string
        """
        country = State()
        self.assertEqual(str, type(country.id))

    def test_save(self):
        """ Test the idType of the class """
        country = State()
        self.assertEqual(str, type(country.id))

    def test_save(self):
        """ Test the save method """
        country = State()
        oldtime = country.updated_at
        country.save()
        self.assertNotEqual(country.updated_at, oldtime)

    def test_save_created_at(self):
        """ Check if class attribute is constant """
        country = State()
        old_created_at = country.created_at
        country.save()
        self.assertEqual(country.created_at, old_created_at)

    def test_updated_at(self):
        """ Tests if save-time updates """
        country = State()
        country.save()
        self.assertNotEqual(country.created_at, country.updated_at)

    def test_display(self):
        """ Test the display of the class """
        country = State()
        disp = f"[State] ({country.id}) {country.__dict__}"
        self.assertEqual(disp, country.__str__())

    def test_dict(self):
        """ Test the dictionary public method """
        country = State()
        self.assertIn('__class__', country.to_dict())
        self.assertIn('created_at', country.to_dict())
        self.assertIn('updated_at', country.to_dict())
