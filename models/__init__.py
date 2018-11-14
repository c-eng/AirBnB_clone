#!/usr/bin/python3


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.user import User

class_list = ["BaseModel"]
for x in BaseModel.__subclasses__():
    class_list.append(x.__name__)

__all__ = class_list

storage = FileStorage()
storage.reload()
