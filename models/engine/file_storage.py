#!/usr/bin/python3
"""FileStorage Module
"""
import json


class FileStorage():
    """FileStorage Class
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds objects
        """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes objects
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Deserializes objects
        """
        try:
            with open(FileStorage.__file_path, 'w') as f:
                FileStorage.__objects = json.load(f)
        except(OSError(errno.ENOENT)):
            pass
