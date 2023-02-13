#!/usr/bin/python3
"""
This module implements the functionalities of BaseModel
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This class serves as base class for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize instances of the class model
        """
        from models import storage
        if kwargs:
            for k, v, in kwargs.items():
                if k != '__class__':
                    if k in ("created_at", "updated_at"):
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of object in the form
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Update the instance updated_at attribute
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the
        instance:
        by using self.__dict__, only instance attributes set will be returned
        key __class__ must be added to this dictionary with the class name of
        the object created_at and updated_at must be converted to string
        object in ISO format:
        format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        you can use isoformat() of datetime object
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                dict_copy[k] = v.isoformat()
        return dict_copy
