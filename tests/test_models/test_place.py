#!/usr/bin/python3
"""
unit test for Area_storage
"""
import unittest
from models.place import Place


class testPlace(unittest.TestCase):
    """
        Test the Place class
    """
    def test_unique_uuid(self):
        """ Test if the id of Area is unique """
        Area = Place()
        Area2 = Place()
        self.assertNotEqual(Area.id, Area2.id)

    def test_attributes(self):
        """ Test if variables can be assigned to class """
        Area = Place()
        self.assertEqual(Area.city_id, '')
        self.assertEqual(Area.user_id, '')
        self.assertEqual(Area.name, '')
        self.assertEqual(Area.description, '')
        self.assertEqual(Area.number_rooms, 0)
        self.assertEqual(Area.number_bathrooms, 0)
        self.assertEqual(Area.max_guest, 0)
        self.assertEqual(Area.price_by_night, 0)
        self.assertEqual(Area.latitude, 0.0)
        self.assertEqual(Area.longitude, 0.0)
        self.assertEqual(Area.amenity_ids, [])
        Area.city_id = "Area - 041B"
        Area.user_id = "Person - A3"
        Area.name = "Trad Society"
        Area.description = "Location at 5th avenue"
        Area.number_rooms = 11
        Area.number_bathrooms = 5
        Area.max_guest = 178
        Area.price_by_night = 600
        Area.latitude = 3.4586
        Area.longitude = 9.321
        self.assertEqual(Area.city_id, "Area - 041B")
        self.assertEqual(Area.user_id, "Person - A3")
        self.assertEqual(Area.name, "Trad Society")
        self.assertEqual(Area.description, "Location at 5th avenue")
        self.assertEqual(Area.number_rooms, 11)
        self.assertEqual(Area.number_bathrooms, 5)
        self.assertEqual(Area.max_guest, 178)
        self.assertEqual(Area.price_by_night, 600)
        self.assertEqual(Area.latitude, 3.4586)
        self.assertEqual(Area.longitude, 9.321)

    def test_idType(self):
        """
        test if id a string
        """
        Area = Place()
        self.assertEqual(str, type(Area.id))

    def test_save(self):
        """ Test the idType of the class """
        Area = Place()
        self.assertEqual(str, type(Area.id))

    def test_save(self):
        """ Test the save method """
        Area = Place()
        oldtime = Area.updated_at
        Area.save()
        self.assertNotEqual(Area.updated_at, oldtime)

    def test_save_created_at(self):
        """ Check if class attribute is constant """
        Area = Place()
        old_created_at = Area.created_at
        Area.save()
        self.assertEqual(Area.created_at, old_created_at)

    def test_updated_at(self):
        """ Tests if save-time updates """
        Area = Place()
        Area.save()
        self.assertNotEqual(Area.created_at, Area.updated_at)

    def test_display(self):
        """ Test the display of the class """
        Area = Place()
        disp = f"[Place] ({Area.id}) {Area.__dict__}"
        self.assertEqual(disp, Area.__str__())

    def test_dict(self):
        """ Test the dictionary public method """
        Area = Place()
        self.assertIn('__class__', Area.to_dict())
        self.assertIn('created_at', Area.to_dict())
        self.assertIn('updated_at', Area.to_dict())
