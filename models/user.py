#!/usr/bin/python3
"""defining user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inheriting from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
