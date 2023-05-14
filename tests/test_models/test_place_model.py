#!/usr/bin/python3

""" module containing tests for class place """

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestUser(unittest.TestCase):
    """ tests for class place """

    def setUp(self):
        """ set up instances for all tests """
        self.test_place = Place()

    def TearDown(self):
        pass

    def test_Place_inheritance(self):
        """ test that place is a subclass of basemodel """

        self.assertIsInstance(self.test_place, BaseModel)

    def test_Place_attributes(self):
        """ test attributes """
        self.assertTrue("city_id" in self.test_place.__dir__())
        self.assertTrue("user_id" in self.test_place.__dir__())
        self.assertTrue("description" in self.test_place.__dir__())
        self.assertTrue("name" in self.test_place.__dir__())
        self.assertTrue("number_rooms" in self.test_place.__dir__())
        self.assertTrue("max_guest" in self.test_place.__dir__())
        self.assertTrue("price_by_night" in self.test_place.__dir__())
        self.assertTrue("latitude" in self.test_place.__dir__())
        self.assertTrue("longitude" in self.test_place.__dir__())
        self.assertTrue("amenity_ids" in self.test_place.__dir__())

    def test_type_longitude(self):
        """ test attributes """
        longitude = getattr(self.test_place, "longitude")
        self.assertIsInstance(longitude, float)

    def test_type_latitude(self):
        """ test attributes """
        latitude = getattr(self.test_place, "latitude")
        self.assertIsInstance(latitude, float)

    def test_type_amenity(self):
        """ test attributes """
        amenity = getattr(self.test_place, "amenity_ids")
        self.assertIsInstance(amenity, list)

    def test_type_price_by_night(self):
        """ test attributes """
        price_by_night = getattr(self.test_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_type_max_guest(self):
        """ test attributes """
        max_guest = getattr(self.test_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_type_number_bathrooms(self):
        """ test attributes """
        number_bathrooms = getattr(self.test_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_type_number_rooms(self):
        """ test attributes """
        number_rooms = getattr(self.test_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_type_description(self):
        """ test attributes """
        description = getattr(self.test_place, "description")
        self.assertIsInstance(description, str)

    def test_type_name(self):
        """ test name """
        name = getattr(self.test_place, "name")
        self.assertIsInstance(name, str)

    def test_type_user_id(self):
        """ test id """
        user_id = getattr(self.test_place, "user_id")
        self.assertIsInstance(user_id, str)

    def test_type_city_id(self):
        """ test id """
        city_id = getattr(self.test_place, "city_id")
        self.assertIsInstance(city_id, str)
