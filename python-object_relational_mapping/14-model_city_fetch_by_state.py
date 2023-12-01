#!/usr/bin/python3
"""prints all City objects from the database """
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """connecting to database"""
    con = "mysql://{}:{}@localhost:{}/{}".format(
        argv[1], argv[2], 3306, argv[3])
    engine = create_engine(con)
    make_session = sessionmaker(bind=engine)
    session = make_session()
    res = session.query(
        State.name, City.id, City.name).join(
        City, State.id == City.state_id).all()
    for i in res:
        print("{}: ({}) {}".format(i[0], i.id, i.name))
        