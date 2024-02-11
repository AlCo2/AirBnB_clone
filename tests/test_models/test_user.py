#!/usr/bin/python3
"""
unit test for person_storage
"""
import unittest
from models.user import User


class testUser(unittest.TestCase):
    """
        Test the User class
    """
    def test_unique_uuid(self):
        """ Test if the id of person is unique """
        person = User()
        person2 = User()
        self.assertNotEqual(person.id, person2.id)

    def test_attributes(self):
        """ Test if variables can be assigned to class """
        person = User()
        self.assertEqual(person.first_name, '')
        self.assertEqual(person.last_name, '')
        self.assertEqual(person.email, '')
        self.assertEqual(person.password, '')
        person.first_name = "Unittest"
        person.last_name = "User"
        person.email = "person@user.com"
        person.password = "reallybasemodel"
        self.assertEqual(person.first_name, 'Unittest')
        self.assertEqual(person.last_name, 'User')
        self.assertEqual(person.email, 'person@user.com')
        self.assertEqual(person.password, 'reallybasemodel')

    def test_idType(self):
        """
        test if id a string
        """
        person = User()
        self.assertEqual(str, type(person.id))

    def test_save(self):
        """ Test the idType of the class """
        person = User()
        self.assertEqual(str, type(person.id))

    def test_save(self):
        """ Test the save method """
        person = User()
        oldtime = person.updated_at
        person.save()
        self.assertNotEqual(person.updated_at, oldtime)

    def test_save_created_at(self):
        """ Check if class attribute is constant """
        person = User()
        old_created_at = person.created_at
        person.save()
        self.assertEqual(person.created_at, old_created_at)

    def test_updated_at(self):
        """ Tests if save-time updates """
        person = User()
        person.save()
        self.assertNotEqual(person.created_at, person.updated_at)

    def test_display(self):
        """ Test the display of the class """
        person = User()
        disp = f"[User] ({person.id}) {person.__dict__}"
        self.assertEqual(disp, person.__str__())

    def test_dict(self):
        """ Test the dictionary public method """
        person = User()
        self.assertIn('__class__', person.to_dict())
        self.assertIn('created_at', person.to_dict())
        self.assertIn('updated_at', person.to_dict())
