#!/usr/bin/python3
"""
 a script that deletes all State objects
 with a name containing the letter a
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
    letter_a = new_session.query(State).filter(State.name.like('%a%'))

    for row in letter_a:
        new_session.delete(row)
    new_session.commit()
    new_session.close()
