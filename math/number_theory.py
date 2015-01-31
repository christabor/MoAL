# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import section
from generic_helpers import _print
from random import randrange as rr
from pprint import pprint as ppr
from fractions import Fraction as frac
from inspect import getsource
from math import log

# Theory references and exercises from
# http://www.math.brown.edu/~jhs/frint.html
# and http://www.math.utah.edu/~carlson/notes/python.pdf


def rand(max_nums):
    for n in range(1, max_nums):
        yield rr(1, max_nums)
    raise StopIteration


def triangle(max_nums):
    for n in range(1, max_nums):
        yield (n * (n + 1)) // 2
    raise StopIteration


def square(max_nums):
    for n in range(1, max_nums):
        yield n * n
    raise StopIteration


def cube(max_nums):
    for n in range(1, max_nums):
        yield n * n * n
    raise StopIteration


def exp(max_nums):
    for n in range(1, max_nums):
        yield n ** n
    raise StopIteration


def exp_custom(max_nums, power):
    for n in range(1, max_nums):
        yield n ** power
    raise StopIteration


def lg(max_nums):
    for n in range(1, max_nums):
        yield log(n)
    raise StopIteration


def lg_custom(max_nums, base):
    if base < 2:
        base = 2
    for n in range(1, max_nums):
        yield log(n, base)
    raise StopIteration


def odd(max_nums):
    for n in range(1, max_nums):
        if n % 3 == 0:
            yield n
    raise StopIteration


def even(max_nums):
    for n in range(1, max_nums):
        if n % 2 == 0:
            yield n
    raise StopIteration


def factor(num):
    div = 2
    factors = []
    # Num is continually divided until it's LTE 1.
    while num > 1:
        # If no remainder, it's a factor, so append it.
        if num % div == 0:
            factors.append(div)
            # Update n be the next small number
            num //= div
        else:
            div += 1
    yield factors
    raise StopIteration


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorials(max_nums):
    # Recursive generator for each item.
    for n in range(1, max_nums):
        yield factorial(n)


def factor_factorials(max_nums):
    for n in range(1, max_nums):
        res = factorial(n)
        for f in factor(res):
            yield ppr({'factors': f, 'num': n, 'factorial': res})


def lcm(a, b):
    # http://en.wikipedia.org/wiki/
    # Least_common_multiple#Reduction_by_the_greatest_common_divisor
    return abs(a * b) // gcd(a, b)


def fibo(max_nums):
    count = 0
    prev, current = 1, 1
    while count < max_nums:
        result = current + prev
        yield result
        current, prev = result, current
        count += 1
    raise StopIteration


def gcd(a, b):
    if a == 0:
        return b
    return gcd(abs(b % a), a)


# Misc. exercises

def exercise_1_2(max_nums):
    # http://www.math.brown.edu/~jhs/frint.html
    for n in range(1, max_nums):
        if n % 3 == 0:
            summed = sum([_ for _ in range(n)])
            yield n, summed, summed // n
    raise StopIteration


def exercise_2_8(max_nums):
    # http://www.math.brown.edu/~jhs/frint.html
    for n in range(1, max_nums):
        yield frac(1, n) + frac(1, n + 2)
    raise StopIteration


# Testing lattice theoretic identities
# http://en.wikipedia.org/wiki/Least_common_multiple#Lattice-theoretic


def commutative_lcm_laws(a, b):
    assert lcm(a, b) == lcm(b, a)
    assert gcd(a, b) == gcd(b, a)


def associative_lcm_laws(a, b, c):
    assert lcm(a, lcm(b, c)) == lcm(lcm(a, b), c)
    assert gcd(a, gcd(b, c)) == gcd(gcd(a, b), c)


def idempotent_lcm_laws(a, b):
    assert lcm(a, a) == a
    assert gcd(a, a) == a


def absorption_lcm_laws(a, b):
    assert lcm(a, gcd(a, b)) == a
    assert gcd(a, lcm(a, b)) == a

# Helper functions


def test_number(*args):
    func, args = args[0], args[1:]
    try:
        _print(func.func_name, [_ for _ in func(*args)])
    except TypeError:
        _print(func.func_name, func(*args))


section('BEGIN - Number theory')

test_number(odd, 10)
test_number(even, 10)
test_number(exp, 10)
[test_number(exp_custom, 10, n) for n in range(10)]
test_number(lg, 10)
[test_number(lg_custom, 10, n) for n in range(10)]
test_number(square, 10)
test_number(fibo, 10)
test_number(cube, 10)
test_number(rand, 10)
test_number(triangle, 10)
[test_number(gcd, rr(999, 9999), rr(999, 9999)) for _ in range(4)]

funcs = [
    lambda x: x ** 2,
    lambda x: x * 2,
    lambda x: x // 2,
    lambda x: x * x - x // x + x
]

[_print(
    'Series of series with: {}'.format(getsource(f)),
    [map(f, (n for n in range(1, _))) for _ in fibo(8)]) for f in funcs]

[_print(
    'Factor {}'.format(n),
    [f for f in factor(rr(100, 9999))][0]) for n in range(4)]

_print('Factorial', [f for f in factorials(10)])

[f for f in factor_factorials(10)]

# Misc. exercises

test_number(exercise_1_2, 20)
test_number(exercise_2_8, 20)

# Should raise no errors
commutative_lcm_laws(10, 320)
associative_lcm_laws(10, 320, 999)
idempotent_lcm_laws(10, 320)
absorption_lcm_laws(10, 320)
