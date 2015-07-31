# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_simple
from MOAL.helpers.display import annotate
from math import factorial

DEBUG = True if __name__ == '__main__' else False

"""
    Factoradic numeral system:
    en.wikipedia.org/wiki/Factorial_number_system
"""


def factpos(num, pos):
    """Take a number and position and get the position
    factorial multiplied by the number.

    Args:
        num (int) - the integer number to use
        pos (int) - the position to find the factorial over
    Returns:
        (int) - the integer result

    >>> factpos(2, 2)
    >>> 4
    """
    return num * factorial(pos)


@annotate
def decimal_to_factoradic(decimal):

    def _print(cq, p, q, r):
        print('{} / {} = {} r{}'.format(cq, p, q, r))

    """Converts a decimal number to factoradic form.

    Args:
        decimal (int) - the decimal number to convert
    Returns:
        res (int) - the decimal number that has been converted

    >>> decimal_to_factoradic(463)
    >>> 341010
    """
    digits, position = '', 1
    quotient, rem = divmod(decimal, position)
    prev_quotient = quotient
    _print(prev_quotient, position, quotient, rem)
    while quotient != 0:
        # Add digit immediately
        digits += str(rem)
        # Update position and quotient/remainder for next iteration
        position += 1
        # Store a copy of previous quotient for visualization purposes.
        prev_quotient = quotient
        quotient, rem = divmod(quotient, position)
        _print(prev_quotient, position, quotient, rem)
    # Add final remainder after while loop terminates
    digits += str(rem)
    digits = digits[::-1]
    print_simple('dec2fac result', digits)
    return int(digits)


@annotate
def factoradic_to_decimal(factoradic):
    """Converts a factoradic number to decimal form.

    Args:
        factoradic (int) - the factoradic number to convert
    Returns:
        res (int) - the converted decimal

    >>> factoradic_to_decimal('341010')
    >>> 463
    """
    res = 0
    digits = list(str(factoradic))
    positions = list(reversed(range(0, len(digits))))
    print_simple('Positions', positions, newline=False)
    for k, digit in enumerate(digits):
        # digit x k !
        # e.g. 5 x 5 ! = 5 x (5!)
        res += factpos(int(digit), positions[k])
    print_simple('fac2dec result', res, newline=False)
    return res


if DEBUG:
    with Section('Factoradic encoding'):
        assert factpos(2, 2) == 4
        assert factpos(2, 3) == 12
        assert factoradic_to_decimal(341010) == 463
        assert decimal_to_factoradic(463) == 341010
