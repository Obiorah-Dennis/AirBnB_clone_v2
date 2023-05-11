#!/usr/bin/python3
""" module BaseModel that contains the BaseModel class """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel class which is inherited by other classes """

    def __init__(self, *args, **kwargs):
        """ initialize the class """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """ returns string representation of BaseModel """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """ returns a printable string representation of BaseModel """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates the attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing keys/values of BaseModel """
        bm_dct = dict(self.__dict__)
        bm_dct['__class__'] = self.__class__.__name__
        bm_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        bm_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return(bm_dict)
