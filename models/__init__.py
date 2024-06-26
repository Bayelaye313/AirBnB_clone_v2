#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import environ
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# check envirn var to determine storage method
if environ['HBNB_TYPE_STORAGE'] == 'db':
    storage = DBStorage()
    storage.reload()
else:  # file storage selected
    storage = FileStorage()
    storage.reload()