#!/usr/bin/python3
"""
a script that lists all State objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    new_session = Session()

    for class_instance in new_session.query(State, City).filter(State.id ==
                                                                City.state_id):
        print("{}: ({}) {}".format(class_instance.State.name,
                                   class_instance.City.id,
                                   class_instance.City.name))

    new_session.close()
