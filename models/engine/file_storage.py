#!/usr/bin/python3

import json
import models
from os import path
from models.user import User

class FileStorage:
    """ JSON file serialization and deserialization for instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in the objects with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        obj_dict = {}
        for key, val in self.__objects.items():
            obj_dict[key] = val.to_dict()

        with open(self.__file_path, mode='w', encoding="UTF8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserialization of JSON file to __objects """
        try:
            with open(self.__file_path, encoding="UTF8") as f:
                obj_dict = json.load(f)
            for key, val in obj_dict.items():
                class_name = val["__class__"]
                if class_name == 'BaseModel':
                    obj = BaseModel(**val)
                elif class_name == 'User':
                    obj = User(**val)
                else:
                    continue
                self.__objects[key] = obj
        except FileNotFoundError:
            pass

