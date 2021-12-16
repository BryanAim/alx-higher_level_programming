#!/usr/bin/python3
"""
a script that adds the State object “Louisiana”
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
    new_state = State(name='Louisiana')
    new_session.add(new_state)
    new_session.commit()
    print(new_state.id)

    new_session.close()
