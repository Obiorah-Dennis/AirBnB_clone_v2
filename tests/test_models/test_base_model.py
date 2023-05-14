#!/usr/bin/python3

""" module containing tests for class BaseModel """

import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime


class TestBase(unittest.TestCase):
    """ tests for class BaseModel """

    def setUp(self):
        """ set up instances for all tests """
        self.test_model = BaseModel()
        self.test_model.name = "No Problem"

    def TearDown(self):
        """ remove test instances """
        del self.test_model

    def test_id_type(self):
        """ test id """
        self.assertEqual("<class 'str'>", str(type(self.test_model.id)))

    def test_ids_differ(self):
        """ test id """
        new_test = BaseModel()
        self.assertNotEqual(new_test.id, self.test_model.id)

    def test_name(self):
        """ test name of BaseModel instance """
        self.assertEqual("No Problem", self.test_model.name)

    def test_a_updated_created_equal(self):
        """ tests created_at """
        self.assertEqual(self.test_model.updated_at.year,
                         self.test_model.created_at.year)

    def test_save(self):
        """ tests updated_at """
        old_update = self.test_model.updated_at
        self.test_model.save()
        self.assertNotEqual(self.test_model.updated_at, old_update)

    def test_str_overide(self):
        """ tests for instance creation and deletion """
        backup = sys.stdout
        inst_id = self.test_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.test_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(inst_id))
        sys.stdout = backup

    def test_to_dict_type(self):
        """ test to_dict method """
        self.assertEqual("<class 'dict'>",
                         str(type(self.test_model.to_dict())))

    def test_to_dict_class(self):
        """ test to_dict method """

        self.assertEqual("BaseModel", (self.test_model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        """ test to_dict method """
        self.assertEqual("<class 'str'>",
                         str(type((self.test_model.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):
        """ test to_dict method """
        tmp = self.test_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs_instantiation(self):
        """ tests for instance creation and deletion """
        test_model_dict = self.test_model.to_dict()
        new_test = BaseModel(**test_model_dict)
        self.assertEqual(new_test.id, self.test_model.id)

    def test_type_created_at(self):
        """ tests for instance creation and deletion """
        test_model_dict = self.test_model.to_dict()
        new_test = BaseModel(test_model_dict)
        self.assertTrue(isinstance(new_test.created_at, datetime.datetime))

    def test_type_updated_at(self):
        """ tests for instance creation and deletion """
        test_model_dict = self.test_model.to_dict()
        new_test = BaseModel(test_model_dict)
        self.assertTrue(isinstance(new_test.updated_at, datetime.datetime))

    def test_compare_dict(self):
        """ tests for instance creation and deletion """
        test_model_dict = self.test_model.to_dict()
        new_test = BaseModel(**test_model_dict)
        new_test_dict = new_test.to_dict()
        self.assertEqual(test_model_dict, new_test_dict)

    def test_instance_diff(self):
        """ tests for instance creation and deletion """
        test_model_dict = self.test_model.to_dict()
        new_test = BaseModel(test_model_dict)
        self.assertNotEqual(self.test_model, new_test)
