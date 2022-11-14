#!/usr/bin/python3

""" This Module contains the BaseModel class """

import uuid
import datetime
import json


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
            models.storage.new(self)