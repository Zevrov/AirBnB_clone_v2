#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Float
import os


class User(BaseModel):
    """This is the class for user"""
    __tablename__ = "users"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", back_populates="user")
        reviews = relationship("Review", back_populates="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
