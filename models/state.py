#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class
        Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)


