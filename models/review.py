#!/usr/bin/python3
""" Review module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class inherits from BaseModel
    """

    text = ""
    user_id = ""
    place_id = ""
