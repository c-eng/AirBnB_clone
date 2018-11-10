#!/usr/bin/python3
"""BaseModel module
"""
import uuid
import datetime
from models.__init__ import storage


class BaseModel():
    """BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """BaseModel Initilization
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                elif key is "__class__":
                    value = eval(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            x = datetime.datetime.now()
            self.created_at = x
            self.updated_at = x
            storage.new(self)

    def __str__(self):
        """BaseModel Stringification
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """BaseModel update
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """BaseModel to_dict function
        """
        out = {attr.rsplit('__', 1)[-1]: value for attr, value in
               self.__dict__.items()}
        out['__class__'] = self.__class__.__name__
        out['created_at'] = self.created_at.isoformat()
        out['updated_at'] = self.updated_at.isoformat()
        return out
