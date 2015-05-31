# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_error
from helpers.display import print_success

DEBUG = True if __name__ == '__main__' else False


class ControlTableNaive:

    """A control table is effectively any number of lists/arrays
    that allow mapping one set of items to another. In this way, their
    lengths must be the same.

    A dictionary would be more appropriate in many cases, except when
    you want to decouple the input from the output, by using separate data
    structures to store each column of information."""

    def __init__(self, table1, table2):
        self.table1 = table1
        self.table2 = table2

    def process(self, key):
        if len(self.table1) < key:
            raise IndexError('Invalid key for first table!')
        try:
            _key = self.table2[key]
            print_success('Here is the control statement '
                          'you requested: `{}` => `{}`'.format(key, _key))
            return _key
        except IndexError:
            print_error('Could not process key: {}'.format(key))
            return None

if DEBUG:
    with Section('Control Table'):
        table1 = ['A', 'W', 'S', 'D']
        table2 = ['Strafe Left', 'Up', 'Down', 'Strafe Right']
        ct2 = ControlTableNaive(table1, table2)
        ct2.process(0)
        ct2.process(1)
        ct2.process(2)
        ct2.process(3)
