#!/usr/bin/python3
"""class City inherits from BaseModel"""
from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """class City that inherits from BaseModel"""

    state_id = State.id
    name = ""
