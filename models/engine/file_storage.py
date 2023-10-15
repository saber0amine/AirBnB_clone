#!/usr/bin/python3
""" file_storage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes and deserialzes json files """

    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """returns all stores basemodel objects"""
        return self.__objects

    def new(self, obj):
        """adding new object to objects dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """save objects dictionary to file"""
        with open(self.__file_path, 'w') as f:
            diction = {key: value.to_dict() for key, value
                       in self.__objects.items()}
            json.dump(diction, f)

    def reload(self):
        """deserialize JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                diction = json.load(f)
                diction = {key: self.classes[value["__class__"]]
                           (**value) for key, value in diction.items()}
                FileStorage.__objects = diction
        except FileNotFoundError:
            return
