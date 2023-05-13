#!/usr/bin/python3
""" module containing tests for class FileStorage """

import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class testFileStorage(unittest.TestCase):
    """ test for class FileStorage """

    def setUp(self):
        """ set up instances for all tests """
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """ remove test instances """

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_return_type(self):
        """ test all method """
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_new_method(self):
        """ test attributes """
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects_value_type(self):
        """ test instances """
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_file_exists(self):
        """ test JSON serialization and deserialization """
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_read(self):
        """ test JSON serialization and deserialization """
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)

        self.assertTrue(type(content) is dict)

    def test_the_type_file_content(self):
        """ test JSON serialization and deserialization """
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()

        self.assertIsInstance(content, str)

    def test_reload_without_file(self):
        """ test JSON serialization and deserialization """

        try:
            self.storage.reload()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
