#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """alchemy engine"""
    __engine = None
    __session = None

    def __init__(self):
        """wlahy t3bnaaaaa"""
        env = getenv('HBNB_ENV')
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/\
                                      {}".format(
            user, passwd, host, db
        ),
                pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """won't write all of this again"""
        obj_dict = {}
        objects = [User, State, City, Amenity, Place, Review]
        if cls:
            query = self.__session.query(cls)
            for obj in query.all():
                _key = obj.to_dict()['__class__'] + '.' + obj.id
                obj_dict[_key] = obj
            return obj_dict
        elif cls is None:
            for class_ in objects:
                query = self.__session.query(class_)
                for obj in query.all():
                    _key = obj.to_dict()['__class__'] + '.' + obj.id
                    obj_dict[_key] = obj
            return obj_dict

    def new(self, obj):
        """ay 7aga"""
        if obj is not None:
            self.__session.add(obj)
        else:
            return

    def save(self):
        """commits"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """lalalalalal"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        safeSession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(safeSession)()

    def close(self):
        """closes"""
        self.__session.close()
