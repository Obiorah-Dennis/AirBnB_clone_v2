#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            cities_list = []
            for key, obj in models.storage.all(City).items():
                if obj.state_id == self.id:
                    cities_list.append(obj)
            return cities_list
