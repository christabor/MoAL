# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_error
from MOAL.helpers.display import print_success
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import prnt
from MOAL.helpers.trials import run_trials
from MOAL.helpers.trials import _test_speed
from faker import Factory
import psycopg2

DEBUG = True if __name__ == '__main__' else False

faker = Factory.create()


def make_person():
    return {
        'name': faker.name(),
        'email': faker.email(),
        'address': faker.address()}


@_test_speed
def insert_all(max_records):
    peeps = [make_person() for n in range(max_records)]
    prnt('Records to create', peeps)
    cur.executemany("""INSERT INTO people(name, email, address)
            VALUES (%(name)s, %(email)s, %(address)s)""", peeps)


if DEBUG:
    with Section('PostgreSQL (via psycopg2)'):
        # Starting postgresql on mac:
        # `postgres -D /usr/local/var/postgres/data`
        try:
            conn = psycopg2.connect(
                dbname='ctabor', user='ctabor', host='localhost', password='')
            print_success('Successfully connected!')
        except:
            print_error('Could not connect to PostgreSql :(')
            raise Exception

        cur = conn.cursor()
        # Always clean up DB for this demo.
        cur.execute("""DROP TABLE people""")
        cur.execute("""CREATE TABLE people(id serial PRIMARY KEY,
            name varchar, email varchar, address varchar)""")

        print_h2('Adding a bunch of records...')
        run_trials(insert_all, trials=10)
        conn.commit()

        print_h2('Reading all records...')

        cur.execute('SELECT * FROM people;')
        records = cur.fetchall()
        prnt('SQL Records', records)
        # Close up shop to prevent zombie processes, etc.
        cur.close()
