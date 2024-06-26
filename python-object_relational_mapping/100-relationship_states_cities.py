#!/usr/bin/python3
"""Script creates the State 'California' with the City 'San Francisco'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    californa = State(name="California")
    san_francisco = City(name="San Francisco")
    californa.cities.append(san_francisco)

    session.add(californa)
    session.commit()
    session.close()
