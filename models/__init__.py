#!/usr/bin/python3
"""Create a unique storage instance for your application"""

from os import environ

# check envirn var to determine storage method
if environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:  # file storage selected
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()