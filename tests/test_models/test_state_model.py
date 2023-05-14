#!/usr/bin/python3
""" module containing tests for class State """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ tests for class State """

    def test_State_inheritence(self):
        """ test that State is a subclass of basemodel """
        test_state = State()
        self.assertIsInstance(test_state, BaseModel)

    def test_State_attributes(self):
        """ tests name """
        test_state = State()
        self.assertTrue("name" in test_state.__dir__())

    def test_State_attributes_type(self):
        """ tests name attribute """
        test_state = State()
        name = getattr(test_state, "name")
        self.assertIsInstance(name, str)
