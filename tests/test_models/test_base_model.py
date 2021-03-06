#!/usr/bin/python3
""" command module unittest
"""

import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class testBase(unittest.TestCase):
    """ tests Base class
    """

    @classmethod
    def setUpClass(cls):
        """instance setup method
        """
        FileStorage._FileStorage__file_path = 'fyle.json'

    def test_init(self):
        """BaseModel init testing
        """
        bad_dict = {"Bad": "Value", "Good": "Horse", "Waffle": "House"}
        with self.assertRaises(ValueError):
            x = BaseModel(**bad_dict)
        badder_dict = {'id': 'Me',
                       'created_at': '2018-11-13T02:26:25.214632',
                       'updated_at': '2018-11-13T02:26:25.214632'}
        with self.assertRaises(ValueError):
            x = BaseModel(**badder_dict)
        baddest_dict = {'id': '2fdd8a18-c8b9-44f8-a7f8-1f3ac8033d2a',
                        'created_at': 'Yesterday',
                        'updated_at': '2018-11-13T02:26:25.214632'}
        with self.assertRaises(ValueError):
            x = BaseModel(**baddest_dict)
        badderest_dict = {'id': '2fdd8a18-c8b9-44f8-a7f8-1f3ac8033d2a',
                          'created_at': '2018-11-13T02:26:25.214632',
                          'updated_at': 'tomorrow'}
        with self.assertRaises(ValueError):
            x = BaseModel(**badderest_dict)

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
        temp = x.updated_at
        x.save()
        self.assertNotEqual(temp, x.updated_at)

    def test_to_dict(self):
        """ test dictionary rep """
        x = BaseModel()
        good_dict = {"id": x.id, "created_at": x.created_at.isoformat(),
                     "updated_at": x.updated_at.isoformat(),
                     "__class__": x.__class__.__name__}
        self.assertEqual(x.to_dict(), good_dict)

    def test_str(self):
        """ test str rep """
        x = BaseModel()
        good_str = "[{}] ({}) {}".format(x.__class__.__name__,
                                         x.id, x.__dict__)
        self.assertEqual(str(x), good_str)
        y = BaseModel()
        good_str = "[{}] ({}) {}".format(y.__class__.__name__,
                                         y.id, y.__dict__)
        self.assertEqual(str(y), good_str)

    def test_kwargs(self):
        """ test kwargs init """
        x = BaseModel()
        y = BaseModel(**x.to_dict())
        self.assertEqual(x.to_dict(), y.to_dict())
        self.assertNotEqual(x, y)
