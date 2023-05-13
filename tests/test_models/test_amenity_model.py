#!/usr/bin/python3

""" module containing tests for class Amenity """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ tests for class Amenity """

    def test_Amenity_inheritence(self):
        """ test that amenity is a subclass of basemodel """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """ test name """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """ test name """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)
