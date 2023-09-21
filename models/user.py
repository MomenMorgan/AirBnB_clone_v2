#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(
<<<<<<< HEAD
        String(128), nullable=False
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    password = Column(
        String(128), nullable=False
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    first_name = Column(
        String(128), nullable=True
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    last_name = Column(
        String(128), nullable=True
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place',
        cascade="all, delete",
        backref='user'
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else None
    reviews = relationship(
        'Review',
        cascade="all, delete",
        backref='user'
    ) if getenv('HBNB_TYPE_STORAGE') == 'db' else None
=======
        String(128), nullable=False)
    password = Column(
        String(128), nullable=False)
    first_name = Column(
        String(128), nullable=True)
    last_name = Column(
        String(128), nullable=True)
    places = relationship(
        'Place',
        cascade="all, delete",
        backref='user')
    reviews = relationship(
        'Review',
        cascade="all, delete",
        backref='user')
>>>>>>> dfbacf1a61228a0c40040d2513235dba2443b817
