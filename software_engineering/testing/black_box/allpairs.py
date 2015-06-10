# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_success
from helpers.display import print_error
from helpers.display import print_simple
from itertools import permutations

DEBUG = True if __name__ == '__main__' else False


def bigrams(conditions):
    bigrams = []
    for k, condition in enumerate(conditions):
        if k < len(conditions) - 1:
            bigrams.append([conditions[k + 1], condition, True, False])
            bigrams.append([conditions[k + 1], condition, True, True])
            bigrams.append([conditions[k + 1], condition, False, True])
            bigrams.append([conditions[k + 1], condition, False, False])
    return bigrams


if DEBUG:
    with Section('All-pairs testing'):
        conditions = ['user', 'email', 'pass', 'pass2']
        perms = [p for p in permutations(conditions)]
        print_simple('Long way', perms, newline=False)
        print_error('Length: {}'.format(len(perms)), prefix='[LONG]')

        bigrams = bigrams(conditions)
        print_simple('Short (all-pairs) way', bigrams, newline=False)
        print_success('Length: {}'.format(len(bigrams)), prefix='[SHORT]')
