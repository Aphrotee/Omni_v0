#!/usr/bin/python3

""" Movie class module """
from models.base_model import BaseModel


class Movie(BaseModel):
    """ Actor class """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.genre = ''
        self.thumbnail = ''
        self.rated_18 = False
        self.video = ''
