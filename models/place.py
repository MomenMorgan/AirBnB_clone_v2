#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(
        String(60),
        ForeignKey('cities.id'),
        nullable=False)
    user_id = Column(
        String(60),
        ForeignKey('users.id'),
        nullable=False)
    name = Column(
        String(128),
        nullable=False)
    description = Column(
        String(1024),
        nullable=True)
    number_rooms = Column(
        Integer,
        nullable=False,
        default=0)
    number_bathrooms = Column(
        Integer,
        nullable=False,
        default=0)
    max_guest = Column(
        Integer,
        nullable=False,
        default=0)
    price_by_night = Column(
        Integer,
        nullable=False,
        default=0)
    latitude = Column(
        Float)
    longitude = Column(
        Float)
    amenity_ids = []
    reviews = relationship(
        'Review',
        cascade="all, delete",
        backref='place')
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            backref='place_amenities'
        )
    else:
        @property
        def amenities(self):
            """the amenities getter"""
            from models import storage
            amenities_ = []
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_.append(value)
            return amenities_

        @amenities.setter
        def amenities(self, value):
            """adds amenity id to amenity_ids"""
            if type(value) is Amenity:
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """returns the reviews getter """
            from models import storage
            reviews_ = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_.append(value)
            return reviews_
