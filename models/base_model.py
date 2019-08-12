#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


kronos = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class"""
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        if "id" not in kwargs:
            self.id = str(uuid.uuid4())

        if "created_at" in kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     kronos)
        else:
            self.created_at = datetime.now()

        if "updated_at" in kwargs:
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     kronos)
        else:
            self.updated_at = datetime.now()

        for keys, values in kwargs.items():
            if "__class__" not in keys:
                setattr(self, keys, values)
            # models.storage.new(self)

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """delete current instance from storage """
        models.storage.delete(self)

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        mdict = dict(self.__dict__)
        mdict["__class__"] = self.__class__.__name__
        mdict["created_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        mdict["updated_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "_sa_instance_state" in mdict:
            del mdict["_sa_instance_state"]
        return mdict
