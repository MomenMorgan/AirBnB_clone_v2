#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(
            String(60),
            ForeignKey('states.id'),
            nullable=False
<<<<<<< HEAD
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(
            String(128), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
            'Place', cascade='all, delete',
            backref='cities'
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else None
=======
            )
    name = Column(
            String(128), nullable=False
            )
    places = relationship(
            'Place', cascade='all, delete',
            backref='cities'
            )
>>>>>>> dfbacf1a61228a0c40040d2513235dba2443b817
