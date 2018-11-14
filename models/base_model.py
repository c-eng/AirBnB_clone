#!/usr/bin/python3
"""BaseModel module
"""
import uuid
import datetime
import models


class BaseModel():
    """BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """BaseModel Initilization
        """
        if kwargs:
            if not all(key in list(kwargs.keys()) for key in
                       ('created_at', 'updated_at', 'id')):
                raise ValueError('Missing id, created_at, updated_at fields')
            kwargs.pop("__class__")
            for key, value in kwargs.items():
                if key is 'id':
                    uuid.UUID(value)
                if key in ("updated_at", "created_at"):
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """BaseModel Stringification
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """BaseModel update
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """BaseModel to_dict function
        """
        out = {attr.rsplit('__', 1)[-1]: value for attr, value in
               self.__dict__.items()}
        out.update({'__class__': self.__class__.__name__, 'created_at':
                    self.created_at.isoformat(), 'updated_at':
                    self.updated_at.isoformat()})
        return out
