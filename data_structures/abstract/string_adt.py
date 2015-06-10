# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from data_structures.abstract.list import ListADT


class StringADT(ListADT):
    """"Implements the conceptual notion of a string; a list of characters."""

    def __init__(self, value):
        self.items = list(value)

    def __str__(self):
        string = ''
        for val in self.items:
            string += val
        return string

    def __setitem__(self, value, _):
        for val in list(value):
            self.items.append(val)

if __name__ == '__main__':
    with Section('String Abstract Data Type'):
        wut = StringADT('Supercalifragalisticexpialido')
        print(wut)
        wut['cious'] = ''
        print(wut)
