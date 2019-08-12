#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class Review(BaseModel, Base):
    """This is the class for Review"""
    __tablename__ = "reviews"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        place = relationship("Place", back_populates="place")

    else:
        place_id = ""
        user_id = ""
        text = ""
