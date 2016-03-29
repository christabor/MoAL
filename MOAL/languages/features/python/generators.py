# -*- coding: utf-8 -*-

"""Python generators examples."""

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

import os

from MOAL.helpers.display import (
    Section,
    print_h2,
    prnt,
)

DEBUG = True if __name__ == '__main__' else False


def get_nums():
    """Just yield some numbers forever - a somewhat canonical example."""
    i = 0
    while True:
        yield i
        print(i)
        i += 1


def product():
    """Keep multiplying nums."""
    prod = 1
    i = 1
    while True:
        yield i
        print('Product is: {} | current `i` is: {}'.format(prod, i))
        prod *= i
        i += 1


def get_some_data(session, limit=1000):
    """A fake session (sqlAlchemy style) for lazy getting of records."""
    offset = 0
    while True:
        f = session.query().offset(offset).limit(limit)
        yield f
        # Update the offset - aka "query pagination".
        offset += limit


def readfile(filename):
    """Read a file, without loading into memory."""
    with open(filename, 'r+') as tempfile:
        while True:
            data = tempfile.read(1024)
            if not data:
                raise StopIteration
            prnt('Read line ================ ', data)
            yield data


def gen_largefile(filename='file.gz', size=1024):
    """Generate a random, large file."""
    f = os.listdir('.')
    if filename not in f:
        os.system('dd if=/dev/urandom of={filename} '
                  'count={size} bs=1024'.format(filename=filename, size=size))


if DEBUG:
    with Section('Language features - generators (lazy evaluation)'):
        numgen = get_nums()
        for _ in range(10):
            next(numgen)
        # Keep running if we want...
        next(numgen)
        next(numgen)
        # Even get the value
        assert next(numgen) == 12
        # The first time this is run will be quite slow -- running
        # the file again should be completely fine.
        # You can also run the command straight in your terminal.
        gen_largefile(size=1024000)  # 1GB
        reader = readfile(os.getcwd() + '/file.gz')
        print(reader)
        next(reader)
        next(reader)
        for _ in range(5):
            next(reader)

        prodgen = product()
        for _ in range(100):
            next(prodgen)

        print_h2('Generator expressions')
        # This won't work (MemoryError),
        # as range is still called and loaded into memory - *lame*.
        # genexpr = (f for f in range(1000000000000))
        # These work, but it is hard to argue their usefulness.
        genexpr = (f for f in get_nums())
        genexpr2 = (f for f in range(100))  # This still loads into memory.
        print(genexpr)
        for _ in range(10):
            next(genexpr)
        # Keep running if we want...
        next(genexpr)
        next(genexpr)
        # Even get the value
        assert next(genexpr) == 12
