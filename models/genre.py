#!/usr/bin/python3

""" Genre class module """
from models.base_model import BaseModel


class Genre(BaseModel):
    """ Genre class """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.comedy = False
        self.historical = False
        self.romance = False
        self.tragedy = False
