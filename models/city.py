#!/usr/bin/python3
""" City module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ City class inherits from BaseModel
    """

    state_id = ""
    name = ""
