#!/usr/bin/python3
"""a script that lists all State objects
that contain the letter a from the database"""
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
    res = session.query(State).distinct().filter(
        State.name.like("%{}%".format(argv[4]))).all()
    if not res:
        print("Not found")
    else:
        for i in res:
            print("{}".format(i.id))
            