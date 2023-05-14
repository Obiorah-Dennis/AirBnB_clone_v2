#!/usr/bin/python3

""" module containing tests for class Review """

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ tests for class Review """

    def test_Review_inheritance(self):
        """ test that Review is a subclass of basemodel """
        test_review = Review()
        self.assertIsInstance(test_review, BaseModel)

    def test_Review_attributes(self):
        """ test attributes """
        test_review = Review()
        self.assertTrue("place_id" in test_review.__dir__())
        self.assertTrue("user_id" in test_review.__dir__())
        self.assertTrue("text" in test_review.__dir__())

    def test_Review_attributes(self):
        """ test attributes """
        test_review = Review()
        place_id = getattr(test_review, "place_id")
        user_id = getattr(test_review, "user_id")
        text = getattr(test_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
