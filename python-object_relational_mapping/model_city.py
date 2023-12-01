#!/usr/bin/python3
"""Module that contains the class definition of a City """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import MySQLdb


class City(Base):
    """ def class City """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )


if __name__ == "__main__":
    connection = MySQLdb(
        host='localhost',
        port=3306
    )
    