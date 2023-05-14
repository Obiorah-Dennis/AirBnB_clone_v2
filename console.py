#!/usr/bin/python3
"""
Command interpreter to manage AirBnB clone objects.
"""
import cmd
import sys
import shlex
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "
    valid_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, args):
        """Creates a new instance of a class, saves it, and prints its id."""
        if len(args) == 0:
            print("** class name missing **")
            return

        try:
            args = shlex.split(args)
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return

            new_instance = self.valid_classes[class_name]()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(str(e))

    def do_show(self, args):
        """Prints the string representation of an instance."""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        key = class_name + "." + instance_id
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        key = class_name + "." + instance_id
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances, or of a specific class."""
        storage = FileStorage()
        storage.reload()
        objects = storage.all()

        if len(args) > 0:
            class_name = args.split()[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return

            instances = [str(obj) for key, obj in objects.items() if key.split(".")[0] == class_name]
        else:
            instances = [str(obj) for obj in objects.values()]

        print(instances)

    def

