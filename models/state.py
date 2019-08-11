#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
import os
import models


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", passive_deletes=True, backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """Return all the cities"""
            city_list = [i for i in models.storage.all(City).values()
                         if i.state_id == self.id]
            return city_list
