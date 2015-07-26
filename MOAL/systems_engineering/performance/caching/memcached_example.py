# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_success
from MOAL.helpers.display import print_info
from MOAL.helpers.display import print_warning
from MOAL.helpers.display import print_h2
from MOAL.helpers.trials import test_speed
from uuid import uuid1
from faker import Factory
import psycopg2
import pylibmc

DEBUG = True if __name__ == '__main__' else False
CACHE_KEY = 'people_key_{}'.format(uuid1())
CLIENTS = ['127.0.0.1']

faker = Factory.create()
mclient = pylibmc.Client(CLIENTS, binary=True, behaviors={'tcp_nodelay': True})


def make_person():
    return {
        'name': faker.name(),
        'email': faker.email(),
        'address': faker.address()}


def create_records(max_records):
    peeps = [make_person() for n in range(max_records)]
    cur.executemany("""INSERT INTO cache_table(name, email, address)
            VALUES (%(name)s, %(email)s, %(address)s)""", peeps)
    conn.commit()


@test_speed
def get_records(cur):
    cached = mclient.get(CACHE_KEY)
    if cached:
        print_success('Found the cached version instead')
        return cached
    else:
        print_warning('Looking up SQL Records')
        cur.execute('SELECT * FROM cache_table;')
        records = cur.fetchall()
        conn.commit()
        # Setup caching once loaded
        mclient.set(CACHE_KEY, records)
        return records


def cleanup(cur, conn):
    print_info('Cleaning up...')
    # Always clean up DB for this demo.
    try:
        cur.execute("""DROP TABLE cache_table;""")
    except psycopg2.ProgrammingError:
        conn.commit()
    # Clean up cache as well.
    mclient.delete(CACHE_KEY)


if DEBUG:
    with Section('Memcached'):
        try:
            conn = psycopg2.connect(
                dbname='ctabor', user='ctabor', host='localhost', password='')
        except:
            raise Exception('Could not connect to PostgreSql')
        cur = conn.cursor()
        print_h2('Adding a bunch of records...')
        cleanup(cur, conn)
        cur.execute("""CREATE TABLE cache_table(id serial PRIMARY KEY,
            name varchar, email varchar, address varchar)""")
        # Create a bunch of initial records
        create_records(5000)
        # Query the database for the newly created records.
        get_records(cur)
        # Read the database again, which will hit memcached first.
        get_records(cur)
        # Close up shop to prevent zombie processes, etc.
        cur.close()
