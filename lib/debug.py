#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy_sandbox import Student, Base

engine = create_engine('sqlite:///students.db')

if __name__ == '__main__':
    import ipdb; 
    Base.metadata.create_all(engine)
    ipdb.set_trace()
