#!/usr/bin/python3
"""script that deletes all State objects with a name containing the
letter 'a' from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).filter(State.name.
                                                                like('%a%')):
        session.delete(state)
    session.commit()
    session.close()
