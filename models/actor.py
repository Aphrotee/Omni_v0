#!/usr/bin/python3

""" Actor class module """
from models.base_model import BaseModel


class Actor(BaseModel):
    """ Actor class """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.movie = ''
        self.gender = ''
        self.first_name = ''
        self.last_name = ''
