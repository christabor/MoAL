# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class Person:

    def __init__(self, **kwargs):
        self.props = kwargs

    def _get_prop(self, prop):
        """Information for accessing properties directly is hidden under
        the private method."""
        if prop in self.props:
            return self.props[prop]
        else:
            return None

    def get_full_name(self):
        """The public 'interface' to getting name values."""
        return '{}. {} {}, {}'.format(
            self._get_prop('prefix'),
            self._get_prop('fname'),
            self._get_prop('lname'),
            self._get_prop('suffix'))


if DEBUG:
    with Section('GRASP information hiding/information expert pattern'):
        print('Name accessed via public method, using hidden information:')
        person = Person(
            fname='Kurt',
            lname='Godel',
            prefix='Mr',
            suffix='Sr'
        )
        print(person.get_full_name())
