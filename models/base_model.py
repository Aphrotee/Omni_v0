#!/usr/bin/python3

""" This Module contains the BaseModel class """

import uuid
import datetime


class BaseModel:
    """ BaseModel class """
    def __init__(self, *args, **kwargs):
        """ Init method """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """ str method """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ save method """
        self.updated_at = datetime.datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """ to_dict method """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """delete method"""
        from models import storage
        storage.delete(self)
