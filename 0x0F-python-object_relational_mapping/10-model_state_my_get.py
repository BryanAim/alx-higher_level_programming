#!/usr/bin/python3
"""
a script that prints the State object with the name passed
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
    name = new_session.query(State).filter(State.name == (sys.argv[4]))

    try:
        print(name[0].id)
    except:
        print("Not found")

    new_session.close()
