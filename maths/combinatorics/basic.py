# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import _print
from helpers.text import uniqchars
from pprint import pprint as ppr
from itertools import permutations
from itertools import product


def factorial(num):
    steps = []
    res = 1
    if num == 0:
        return [num]
    while num > 1:
        res *= (num)
        num -= 1
        steps.append(res)
    return res, steps


def combochars(max_chars, segments):
    chars = uniqchars(max_chars)
    return permutations(chars, segments)


def group_combochars(length, segments=2):
    if length < segments:
        length = segments
    return [[_ for _ in combochars(n, segments)] for n in range(2, length)]


def cartesian(max_chars, max_nums, unique=False):
    res = [''.join(prod[0]) for prod in product(
        combochars(max_chars, 2), range(0, max_nums))]
    if unique:
        return list(set(res))
    else:
        return res


if __name__ == '__main__':
    with Section('Combinatorics'):
        _print('Unique chars', uniqchars(10))
        fact = factorial(12)
        _print('Final factorial amount:', fact[0])
        ppr(fact[1])
        combos = combochars(4, 2)
        _print('Permutations of random letters', ', '.join(
            [''.join(combo) for combo in combos]))
        _print(
            'Combinations of multiple permutations of random letters',
            group_combochars(6, segments=2), func=ppr)
        _print('Cartesian product of two sets', cartesian(4, 4))
        _print(
            'Cartesian product of two sets (unique)',
            cartesian(4, 4, unique=True))
