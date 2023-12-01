#!/usr/bin/python3
"""a script that prints the first State object from the database"""
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
    res = session.query(State).order_by(State.id).first()
    if res is None:
        print("Nothing")
    else:
        print("{}: {}".format(res.id, res.name))
        