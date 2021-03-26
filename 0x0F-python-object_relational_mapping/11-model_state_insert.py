#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           ("root", "root", argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    louisiana = State(name='Louisiana', id=6)
    session.add(louisiana)
    for state in session.query(State).order_by(State.id).filter(State.name.
                                                                like('%a%')):
        print("{}: {}".format(state.id, state.name))
    session.close()
