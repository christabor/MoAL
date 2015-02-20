# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import _print
from pprint import pprint as ppr


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

        _print('Arg/kwarg unpacking', '')
        f = func(1, 2, 3, cats=True, dogs=True)
        _print('Args/kwargs passing', f, func=ppr)

        orig, squares = nums_and_squares(10)
        _print('Return val (tuple) unpacking', '{}, {}'.format(orig, squares))

        mysandwich = {
            'sandwich': 'Ham & Cheese',
            'slices_cheese': 2,
            'slices_ham': 3
        }

        sand_type, cheeses, hams = mysandwich
        _print('Unpacking keys (default)', '{}, {}, {}'.format(
            sand_type, cheeses, hams))

        sand_type, cheeses, hams = mysandwich.values()
        _print('Unpacking values', '{}, {}, {}'.format(
            sand_type, cheeses, hams))

    with Section('Python - packing'):
        st = 'Ham & Cheese'
        sc = 'slices_cheese'
        sh = 'slices_ham'
        sandwich_tuple = st, sc, sh

        _print(
            ('Passing a packed list to a function '
             '(or, unpacking a list into a function)'),
            div_exp(*[n for n in range(1, 10)]))
