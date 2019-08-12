#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os
import models


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id',
           String(60),
           ForeignKey('places.id'),
           primary_key=True,
           nullable=False),
    Column('amenity_id',
           String(60),
           ForeignKey('amenities.id'),
           primary_key=True,
           nullable=False)
)


class Place(BaseModel, Base):
    """This is the class for Place"""
    __tablename__ = "places"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", back_populates="place")
        amenities = relationship(
            "Amenity", secondary='place_amenity',
            back_populates="places", viewonly=False)
        city = relationship("City", back_populates="places")
        user = relationship("User", back_populates="places")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
	    def reviews(self):
	        """Review Getter"""
	        r_dic = models.storage.all('Review')
	        r_list = []
	        for index in reviews_dict.values():
	            if index.place_id == self.id:
	                r_list.append(index)

	            return i

	    @property
	    def amenities(self):
	        """Getter for amenities"""
	        object_list = []
	        objs = models.storage.all('Amenity')
	        for index in objs.values():
	            if index.id in amenity_id:
	                object_list.append(index)

	            return object_list

	    @amenities.setter
	    def amenities(self, obj):
	        """ameneties setter"""
	        if isinstance(obj, Amenity):
	            if self.id == obj.place_id:
	                self.amenity_ids.append(obj.id)
