#!/usr/bin/python3

from uuid import uuid4 as ui
from datetime import datetime as dt


class BaseModel:
    """Base class for all other model classes"""

    def __init__(self, *args, **kwargs):
        """constructor function"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = dt.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = dt.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(ui())
            self.created_at = dt.now()
            self.updated_at = dt.now()

    def __str__(self):
        """returns human readable format of object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = dt.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
