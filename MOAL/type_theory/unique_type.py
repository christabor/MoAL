# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from functools import wraps

DEBUG = True if __name__ == '__main__' else False

called = []


class UniquelyTypedError(Exception):
    pass


def uniquelytyped(func, *args, **kwargs):
    @wraps(func)
    def _inner(*args, **kwargs):
        if func.__name__ not in called:
            func(*args, **kwargs)
            called.append(func.__name__)
        else:
            raise UniquelyTypedError
    return _inner


@uniquelytyped
def readfile(filename):
    # The example here illustrates a situation where the function may not
    # be referentially transparent, since it might modify the file and thus
    # change future calling scenarios.
    print('Opening file... {}'.format(filename))
    print('File opened.')


if DEBUG:
    with Section('Unique typing'):
        readfile('fakefile.txt')
        # Should not be possible...
        try:
            readfile('fakefile.txt')
        except UniquelyTypedError:
            print('Successfully prevented a unique function from being called.')
