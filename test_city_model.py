#!/usr/bin/python3

""" module containing tests for class City """

import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    """ tests for class City """

    def test_City_inheritance(self):
        """ test that city is a subclass of basemodel """
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        """ test attributes """
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    def test_type_name(self):
        """ test name """
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        """ test name """
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)
