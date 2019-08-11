#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
     __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
                                   secondary=place_amenity)

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
