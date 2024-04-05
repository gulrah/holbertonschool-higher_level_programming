#!/usr/bin/python3
"""Script that prints all City objects from the database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State.name) \
                            .filter_by(id=city.state_id) \
                            .first()[0]
        print("{}: ({}) {}".format(state_name, city.id, city.name))
        session.close()
