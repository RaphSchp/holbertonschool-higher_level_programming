#!/usr/bin/python3
"""a python file that contains the class definition
of a State and an instance Base = declarative_base()"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sys import argv
Base = declarative_base()


class State(Base):
    """claas state that inherits from base"""
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    