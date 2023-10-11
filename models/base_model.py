#!/usr/bin/python3
"""
the class BaseModel defines all common
attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """
    BaseModel defines all common
    attributes/methods for other classes
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """this function returns the string representation
            of an instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dir__)

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.update_at.isoformat()
        return data