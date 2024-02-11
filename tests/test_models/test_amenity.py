#!/usr/bin/python3
"""
unit test for item_storage
"""
import unittest
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    """
        Test the Amenity class
    """
    def test_unique_uuid(self):
        """ Test if the id of item is unique """
        item = Amenity()
        item2 = Amenity()
        self.assertNotEqual(item.id, item2.id)

    def test_attributes(self):
        """ Test if variables can be assigned to class """
        item = Amenity()
        self.assertEqual(item.name, '')
        item.name = "Tool"
        self.assertEqual(item.name, 'Tool')
        item2 = Amenity()
        self.assertNotEqual(item.name, item2.name)
        self.assertEqual(item2.name, '')
        item2.name = 'Box'
        self.assertEqual(item2.name, 'Box')

    def test_idType(self):
        """
        test if id a string
        """
        item = Amenity()
        self.assertEqual(str, type(item.id))

    def test_save(self):
        """ Test the idType of the class """
        item = Amenity()
        self.assertEqual(str, type(item.id))

    def test_save(self):
        """ Test the save method """
        item = Amenity()
        oldtime = item.updated_at
        item.save()
        self.assertNotEqual(item.updated_at, oldtime)

    def test_save_created_at(self):
        """ Check if class attribute is constant """
        item = Amenity()
        old_created_at = item.created_at
        item.save()
        self.assertEqual(item.created_at, old_created_at)

    def test_updated_at(self):
        """ Tests if save-time updates """
        item = Amenity()
        item.save()
        self.assertNotEqual(item.created_at, item.updated_at)

    def test_display(self):
        """ Test the display of the class """
        item = Amenity()
        disp = f"[Amenity] ({item.id}) {item.__dict__}"
        self.assertEqual(disp, item.__str__())

    def test_dict(self):
        """ Test the dictionary public method """
        item = Amenity()
        self.assertIn('__class__', item.to_dict())
        self.assertIn('created_at', item.to_dict())
        self.assertIn('updated_at', item.to_dict())
