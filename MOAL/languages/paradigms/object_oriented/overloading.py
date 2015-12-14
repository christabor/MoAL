# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.generic import verbose

DEBUG = True if __name__ == '__main__' else False


class Person:
    def __init__(self, age, fname, lname):
        self.age = age
        self.fname = fname
        self.lname = lname

    @verbose
    def __int__(self):
        return int(self.age)

    @verbose
    def __le__(self, other):
        return self.age <= other.age

    @verbose
    def __lt__(self, other):
        return self.age < other.age

    @verbose
    def __gt__(self, other):
        return self.age > other.age

    @verbose
    def __eq__(self, other):
        return self.age == other.age

    @verbose
    def __ge__(self, other):
        return self.age >= other.age


class SuperSaiyan:

    @verbose
    def __init__(self, *args, **kwargs):
        print('KAMEEEYAAAMEEEYAAA')


class Saiyan:

    @verbose
    def __add__(self, other):
        return SuperSaiyan()


if DEBUG:
    with Section('Operator overloading'):
        norbert = Person(23, 'Norbert', 'Flombo')
        terminus = Person(101010, 'Terminus', 'Maximus')
        print(norbert < terminus)
        print(norbert > terminus)
        print(norbert == terminus)
        print(int(norbert))

        vegeta = Saiyan() + Saiyan()
        print(vegeta)
