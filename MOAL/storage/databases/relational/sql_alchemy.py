# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import prnt
from MOAL.helpers.trials import run_trials
from MOAL.helpers.trials import test_speed
from MOAL.helpers.datamaker import random_person
from faker import Factory
from pprint import pprint as ppr

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DEBUG = True if __name__ == '__main__' else False

faker = Factory.create()
# Use in-memory database for our example.
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
# Setup session
Session = sessionmaker()
Session.configure(bind=engine)
# Configured db with session
db_session = Session()


class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    url = Column(String(255))

    def __repr__(self):
        return '<Person(name={}, email={}, url={})>'.format(
            self.name, self.email, self.url)


@test_speed
def insert_all(max_records):
    people = [random_person() for n in range(max_records)]
    prnt('Records to create:', people)
    for person in people:
        # Don't need this prop for our example schema.
        del person['address']
        db_session.add(Person(**person))

if DEBUG:
    with Section('MySQL - SQL Alchemy'):
        Base.metadata.create_all(engine)

        print_h2('Adding a bunch of records...')
        run_trials(insert_all, trials=10)

        print_h2('Reading all records...')
        recs = db_session.query(Person).all()
        ppr(recs)
