#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class definition of a State"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
