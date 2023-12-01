#!/usr/bin/python3
"""a script that changes the name of
a State object from the database"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """connecting to database"""
    con = "mysql://{}:{}@localhost:{}/{}".format(
        argv[1], argv[2], 3306, argv[3])
    engine = create_engine(con)
    make_session = sessionmaker(bind=engine)
    session = make_session()
    """update state object"""
    new = session.query(State).filter(State.id == 2).first()
    new.name = "New Mexico"
    session.commit()
    