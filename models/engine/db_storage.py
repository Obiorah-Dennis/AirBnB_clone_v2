#!/usr/bin/python3
"""
The engine linked to a MySql database for ORM
"""
import sqlalchemy
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models


class DBStorage:
    """
    SQLAlchemy storage engine for HBNB
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialization for class DBStorage
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        my_sqldb = "mysql+mysqldb://{}:{}@{}/{}".format(user,
                                                        password,
                                                        host,
                                                        database)
        self.__engine = create_engine('{}'.format(my_sqldb),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session) all
        objects depending of the class name (argument cls)
        """
        db_query = []
        newsql_dict = {}
        if cls is not None:
            results = self.__session.query(cls).all()
            for row in results:
                key = row.__class__.__name__ + '.' + row.id
                newsql_dict[key] = row
        else:
            for key, value in models.classes.items():
                try:
                    self.__session.query(models.classes[key]).all()
                    db_query.append(models.classes[key])
                except BaseException:
                    continue
            for classes in db_query:
                results = self.__session.query(classes).all()
                for row in results:
                    key = row.__class__.__name__ + '.' + row.id
                    newsql_dict[key] = row
        return newsql_dict

    def new(self, obj):
        """
        add the object to the current database
        session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current
        database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database
        session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        (feature of SQLAlchemy) andcreate the current
        database session (self.__session) from the engine
        (self.__engine) by using a sessionmaker
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        ends the SQLAlchemy session
        """
        self.__session.close()
