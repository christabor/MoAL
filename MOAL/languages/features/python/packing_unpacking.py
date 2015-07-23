# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import prnt


def func(*args, **kwargs):
    def inner_func(*args, **kwargs):
        for arg in args:
            print(arg)
        for kwarg in kwargs:
            print(kwarg)
        return args, kwargs
    return inner_func(*args, **kwargs)


def nums_and_squares(max_nums):
    return range(0, max_nums), [n * n for n in range(max_nums)]


def div_exp(*nums):
    return [n ** n // n for n in nums]

if __name__ == '__main__':
    with Section('Python - unpacking'):

        prnt('Arg/kwarg unpacking', '')
        f = func(1, 2, 3, cats=True, dogs=True)
        prnt('Args/kwargs passing', f)

        orig, squares = nums_and_squares(10)
        prnt('Return val (tuple) unpacking', '{}, {}'.format(orig, squares))

        mysandwich = {
            'sandwich': 'Ham & Cheese',
            'slices_cheese': 2,
            'slices_ham': 3
        }

        sand_type, cheeses, hams = mysandwich
        prnt('Unpacking keys (default)', '{}, {}, {}'.format(
            sand_type, cheeses, hams))

        sand_type, cheeses, hams = mysandwich.values()
        prnt('Unpacking values', '{}, {}, {}'.format(
            sand_type, cheeses, hams))

    with Section('Python - packing'):
        st = 'Ham & Cheese'
        sc = 'slices_cheese'
        sh = 'slices_ham'
        sandwich_tuple = st, sc, sh

        prnt(
            ('Passing a packed list to a function '
             '(or, unpacking a list into a function)'),
            div_exp(*[n for n in range(1, 10)]))
