#!/usr/bin/python3

import unittest
from datetime import datetime, timedelta
from models.basemodel import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """
        initializes a BaseModel instance before each test,
        rather than repetition
        """
        self.model = BaseModel()

    def test_initialization(self):
        """
        checks that objects are equal initially
        """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_save_method(self):
        """
        Ensures that updated_at is updated when save is called
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)

    def test_to_dict(self):
        """
        Verifies that the dictionary representation includes the correct
        values & formats
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

    def test_str_method(self):
        """
        confirms the string representation of the basemodel
        """
        model_str = str(self.model)
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(model_str, expected_str)

if __name__ == '__main__':
    unittest.main()
