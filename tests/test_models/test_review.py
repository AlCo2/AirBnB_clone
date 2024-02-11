#!/usr/bin/python3
"""
unit test for comment_storage
"""
import unittest
from models.review import Review


class testReview(unittest.TestCase):
    """
        Test the Review class
    """
    def test_unique_uuid(self):
        """ Test if the id of comment is unique """
        comment = Review()
        comment2 = Review()
        self.assertNotEqual(comment.id, comment2.id)

    def test_attributes(self):
        """ Test if variables can be assigned to class """
        comment = Review()
        self.assertEqual(comment.place_id, '')
        self.assertEqual(comment.user_id, '')
        comment.name = "Jonathan"
        comment.user_id = "009-213"
        self.assertEqual(comment.name, 'Jonathan')
        self.assertEqual(comment.user_id, '009-213')

    def test_idType(self):
        """
        test if id a string
        """
        comment = Review()
        self.assertEqual(str, type(comment.id))

    def test_save(self):
        """ Test the idType of the class """
        comment = Review()
        self.assertEqual(str, type(comment.id))

    def test_save(self):
        """ Test the save method """
        comment = Review()
        oldtime = comment.updated_at
        comment.save()
        self.assertNotEqual(comment.updated_at, oldtime)

    def test_save_created_at(self):
        """ Check if class attribute is constant """
        comment = Review()
        old_created_at = comment.created_at
        comment.save()
        self.assertEqual(comment.created_at, old_created_at)

    def test_updated_at(self):
        """ Tests if save-time updates """
        comment = Review()
        comment.save()
        self.assertNotEqual(comment.created_at, comment.updated_at)

    def test_display(self):
        """ Test the display of the class """
        comment = Review()
        disp = f"[Review] ({comment.id}) {comment.__dict__}"
        self.assertEqual(disp, comment.__str__())

    def test_dict(self):
        """ Test the dictionary public method """
        comment = Review()
        self.assertIn('__class__', comment.to_dict())
        self.assertIn('created_at', comment.to_dict())
        self.assertIn('updated_at', comment.to_dict())
