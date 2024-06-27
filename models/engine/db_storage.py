#!/usr/bin/python3
"""Define storage engine using MySQL database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage with SQLAlchemy engine and session."""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.
            format(os.getenv('HBNB_MYSQL_USER'),
                   os.getenv('HBNB_MYSQL_PWD'),
                   os.getenv('HBNB_MYSQL_HOST'),
                   os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects from the database."""
        obj_dict = {}

        if cls:
            query_result = self.__session.query(cls).all()
        else:
            query_result = []
            for model in [User, State, City, Amenity, Place, Review]:
                query_result.extend(self.__session.query(model).all())

        for obj in query_result:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Add object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and initialize session."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close the session."""
        self.__session.remove()