#!/usr/bin/python3
"""class Review inherits from BaseModel"""
from models.base_model import BaseModel

class Review(BaseModel):
    """class Review that inherits from BaseModel"""

    place_id= "" #Place.id
    user_id= "" #User.id
    text=  ""
