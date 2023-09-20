#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref='state')
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities():
            """anything"""
            cities_list = []
            for value in storage.all(City).values():
                if value.state_id == State.id:
                    cities_list.append(value)
            return cities_list
