#!/usr/bin/python3
"""
a script that prints the first State object from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    new_session = Session()
    first = new_session.query(State).first()

    if first is None:
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))

    new_session.close()
