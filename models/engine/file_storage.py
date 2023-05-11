#!/usr/bin/python3

import json
from os import path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
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

