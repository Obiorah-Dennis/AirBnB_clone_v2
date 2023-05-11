#!/usr/bin/python3

import json
from os import path


class FileStorage:
    """ JSON file serialization and deserialization for instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary __objects """
        return self.__objects

    def new(self, obj):
        """  sets in the objects with key <obj class name>.id """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        dict_value = obj
        FileStorage.__objects[key] = dict_value

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        obj_dict = {}
        for key, val in FileStorage.__objects.items():
            obj_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as f:
            json.dump(obj_dict, f)

    def reload(self):
<<<<<<< HEAD
        """ deserialization of JSON file to __objects """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as f:
                FileStorage.__objects = json.load(f)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
=======
        if not path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as f:
            obj_dict = json.load(f)

        from models.base_model import BaseModel
        from models.user import User

        class_map = {
            'BaseModel': BaseModel,
            'User': User
            # Add other classes as needed
        }

        for key, obj in obj_dict.items():
            class_name, obj_id = key.split('.')
            obj_dict[key]['created_at'] = datetime.strptime(
                obj_dict[key]['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            obj_dict[key]['updated_at'] = datetime.strptime(
                obj_dict[key]['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.__objects[key] = class_map[class_name](**obj)

>>>>>>> eea822d0526c6f5e51d8c0b41fa3623fc17f74ae
