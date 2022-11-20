#!/usr/bin/python3

""" This Module contains the FileStorage class """

import json
from models.base_model import BaseModel
from models.user import User
from models.actor import Actor
from models.movie import Movie
from models.genre import Genre


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all method """
        return FileStorage.__objects

    def new(self, obj):
        """ new method """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ save method """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """ reload method """
        try:
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)
            for key, value in objs.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
