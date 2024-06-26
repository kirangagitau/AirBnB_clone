#!/usr/bin/python3
"""
use python version 3
this is testing for proper functionality of 
the base_model class
"""

import unittest
from models.base_model import BaseModel

class TestBasemodel(unittest.TestCase):
    def test_init(self):  # testing the constructor.
        my_nodel = Basemodel()

        self.assertIsNotNone(my_model.id)  # be true
        self.assertIsNotNone(my_model.created_at)  # be true
        self.assertIsNotNone(my_model.updated_at)  # be true

    def test_save(self):  # testing save method.
        my_model = BaseModel()

        init_updated_at = my_model.updated_at

        new_updated_at = my_model.save()

        self.assertNotEwual(init_updated_at, new_updated_at)

    def test_to_dict(self):
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)  # should be dict
        self.assertEqual(my_model_dict["__class__", 'BaseModel'])  # correct key
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.created_at.isoformat())

    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startWith(['BaseModel']))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

    if __name__ == "__main__":
        unittest.main()
