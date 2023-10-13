#!/usr/bin/python3
"""class User inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ""
    password = ""
    fifrst_name = ""
    last_name = ""
