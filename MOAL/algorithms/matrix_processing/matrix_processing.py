# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h4
from MOAL.helpers.datamaker import random_matrix
from MOAL.helpers import trials
from pprint import pprint as ppr

DEBUG = True if __name__ == '__main__' else False


def exp_by_squaring(x, n):
    """From Wikipedia: "In mathematics and computer programming,
    exponentiating by squaring is a general method for fast computation of
    large positive integer powers of a number, or more generally of an
    element of a semigroup, like a polynomial or a square matrix.

    Some variants are commonly referred to as square-and-multiply
    algorithms or binary exponentiation. These can be of quite general use,
    for example in modular arithmetic or powering of matrices.
    For semigroups for which additive notation is commonly used,
    like elliptic curves used in cryptography, this method is also
    referred to as double-and-add."

    Algorithm converted from pseudocode at:
    en.wikipedia.org/wiki/Exponentiation_by_squaring
    """
    if n < 0:
        return exp_by_squaring(1 // x, -n)
    if n == 0:
        return 1
    if n == 1:
        return x
    # Is even
    if n % 2 == 0:
        return exp_by_squaring(x * x, n // 2)
    # Is odd
    if n % 2 != 0:
        return x * exp_by_squaring(x * x, (n - 1) // 2)


def exp_by_convential(x, n):
    """This is much faster since it's native."""
    return x ** n


@trials._test_speed
def trial_exp(func, max=10):
    print('Testing function: "{}"'.format(func.__name__))
    rounds = []
    for x in range(max):
        round = []
        for n in range(max):
            round.append(func(x, n))
        rounds.append(round)
    ppr(rounds)
    return rounds


def test_matrix_with_exp(matrix):
    """Test the exponentiation function with a bonafide matrix."""
    ppr(matrix)
    for row in matrix:
        for k in row:
            print(k, exp_by_squaring(k, 2))


if DEBUG:
    with Section('Matrix Processing algorithms'):
        print_h4('Trials with different squaring functions')
        res = trial_exp(exp_by_squaring)
        res2 = trial_exp(exp_by_convential)
        assert res == res2

        print_h4('Trials with squaring function on matrices')
        test_matrix_with_exp(random_matrix(rows=3, columns=3))
