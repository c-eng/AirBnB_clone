#!/usr/bin/python3
""" command module unittest
"""

import unittest
import datetime
from models.base_model import BaseModel


class testBase(unittest.TestCase):
    """ tests Base class
    """

    def test_uuid(self):
        """ uuid test """
        x = BaseModel()
        self.assertEqual(type(x.id), str)
        y = BaseModel()
        self.assertNotEqual(x.id, y.id)

    def test_created_at(self):
        """ test datetime creation """
        x = BaseModel()
        self.assertIsInstance(x.created_at, datetime.datetime)
        self.assertIsInstance(x.updated_at, datetime.datetime)
        self.assertEqual(x.created_at, x.updated_at)

    def test_updated_at(self):
        """ test datetime update """
        x = BaseModel()
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_to_dict(self):
        """ test dictionary rep """
        x = BaseModel()
        good_dict = {"id": x.id, "created_at": x.created_at.isoformat(),
                     "updated_at": x.updated_at.isoformat(),
                     "__class__": "BaseModel"}
        self.assertEqual(x.to_dict(), good_dict)

    def test_str(self):
        """ test str rep """
        x = BaseModel()
        good_str = "[BaseModel] ({}) {}".format(x.id, x.__dict__)
        self.assertEqual(str(x), good_str)

    def test_kwargs(self):
        """ test kwargs init """
        x = BaseModel()
        y = BaseModel(**x.to_dict())
        self.assertEqual(x.to_dict(), y.to_dict())
        self.assertNotEqual(x, y)
