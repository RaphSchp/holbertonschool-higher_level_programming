#!/usr/bin/python3
""" a script that adds the State object
“Louisiana” to the database"""
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
    """add a new state object"""
    session.add(State(name="Louisiana"))
    session.commit()
    new = session.query(State).filter(State.name == "Louisiana").first()
    print(new.id)
    