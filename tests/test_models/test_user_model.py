#!/usr/bin/python3

""" module containing tests for class User """

import unittest
from models.base_model import BaseModel
from models.user import User
from io import StringIO
import sys
import datetime


class TestUser(unittest.TestCase):
    """ tests for class User """

    def test_User_inheritance(self):
        """ test that User is a subclass of basemodel """
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_User_attributes(self):
        """ test attributes """

        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    def test_type_email(self):
        """ test name """
        new = User()
        name = getattr(new, "email")
        self.assertIsInstance(name, str)

    def test_type_first_name(self):
        """ test name """
        new = User()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    def test_type_last_name(self):
        """ test name """
        new = User()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    def test_type_password(self):
        """ test password """
        new = User()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)
