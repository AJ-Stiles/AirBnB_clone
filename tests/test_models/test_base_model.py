#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_attributes(self):
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        self.assertEqual(model.name, "Test Model")
        self.assertEqual(model.my_number, 42)

    def test_str_method(self):
        model = BaseModel()
        str_rep = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), str_rep)

    def test_save_method(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(model_dict["created_at"],
                         model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         model.updated_at.isoformat())

    def test_instance_from_dict(self):
        my_dict = {
            'id': '12345',
            'created_at': '2023-08-01T12:00:00.000000',
            'name': 'Sample Name',
            'my_number': 42
        }
        my_model = BaseModel(**my_dict)
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(my_model.id, '12345')
        self.assertEqual(my_model.created_at,
                         datetime.strptime('2023-08-01T12:00:00.000000',
                                           '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(my_model.name, 'Sample Name')
        self.assertEqual(my_model.my_number, 42)


if __name__ == '__main__':
    unittest.main()
