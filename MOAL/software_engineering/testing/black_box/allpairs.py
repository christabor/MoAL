# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_success
from MOAL.helpers.display import print_error
from MOAL.helpers.display import print_simple
from itertools import permutations

DEBUG = True if __name__ == '__main__' else False


def bigrams(conditions):
    _bigrams = []
    for k, condition in enumerate(conditions):
        if k < len(conditions) - 1:
            _bigrams.append([conditions[k + 1], condition, True, False])
            _bigrams.append([conditions[k + 1], condition, True, True])
            _bigrams.append([conditions[k + 1], condition, False, True])
            _bigrams.append([conditions[k + 1], condition, False, False])
    return _bigrams


if DEBUG:
    with Section('All-pairs testing'):
        conditions = ['user', 'email', 'pass', 'pass2']
        perms = [p for p in permutations(conditions)]
        print_simple('Long way', perms, newline=False)
        print_error('Length: {}'.format(len(perms)), prefix='[LONG]')

        bgrams = bigrams(conditions)
        print_simple('Short (all-pairs) way', bgrams, newline=False)
        print_success('Length: {}'.format(len(bgrams)), prefix='[SHORT]')
