#!/usr/bin/python3

""" module containing tests for class Amenity """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ tests for class Amenity """

    def test_Amenity_inheritence(self):
        """ test that amenity is a subclass of basemodel """
        test_amenity = Amenity()
        self.assertIsInstance(test_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """ test name """
        test_amenity = Amenity()
        self.assertTrue("name" in test_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """ test name """
        test_amenity = Amenity()
        name_value = getattr(test_amenity, "name")
        self.assertIsInstance(name_value, str)
