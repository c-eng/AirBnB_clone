#!/usr/bin/python3
""" engine module unittest
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class testStorage(unittest.TestCase):
    """tests FileStorage class
    """

    @classmethod
    def setUpClass(cls):
        """instance setup method
        """
        FileStorage._FileStorage__file_path = 'fyle.json'

    def test_file(self):
        """file creation test
        """
        x = FileStorage()
        x.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))

    def test_io(self):
        """Testing file io
        """
        temp = {'BaseModel.1654beb8-6c65-4733-9b53-76f0f20631f1':
                {'updated_at': '2018-11-13T03:51:08.897684',
                 'created_at': '2018-11-13T03:51:08.897684',
                 '__class__': 'BaseModel',
                 'id': '1654beb8-6c65-4733-9b53-76f0f20631f1'}}
        FileStorage._FileStorage__objects = temp
        storage.save()
        storage.reload()
        self.assertEqual(temp, FileStorage._FileStorage__objects)
