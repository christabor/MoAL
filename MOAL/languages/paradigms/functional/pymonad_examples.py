# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.datamaker import random_person
import pymonad as pm
from pprint import pprint as ppr


DEBUG = True if __name__ == '__main__' else False


@pm.curry
def add2(x, y):
    return x + y


@pm.curry
def add_ten_to(x, y):
    return x + y + 10


@pm.curry
def add3(x, y, z):
    return x + y + z


@pm.curry
def add(x, y):
    return x + y


@pm.curry
def sub2(x):
    return x - 2


@pm.curry
def neg(x):
    return -x


def foofix(word):
    return 'FOO_' + word


def negafy(*vals):
    """Take a list of values and convert them to negatives with the List
    monoid and the negative function composition."""
    return neg * pm.List(*vals)


def num_and_ranges(x):
    """Return the List monoid and lists of values and
    negative to positive ranges for a maximum"""
    return pm.List(*(x, range(-x, x + 1)))


def monadify(*funcs):
    _monad = pm.List()
    for func in funcs:
        _monad >> func
    return _monad


def sqr(x):
    return pm.List(x, x ** 2)


@pm.curry
def exp(x, pow):
    return pm.List(x, x ** pow)


def monoid_range(max):
    """Like python range, but in monoid form instead."""
    return pm.List(*range(max))


@pm.curry
def s_add(x, y):
    return pm.State(lambda old: (x + y, old + 1))


@pm.curry
def s_sub(x, y):
    return pm.State(lambda old: (x + y, old + 1))


@pm.curry
def s_exp(x, y):
    return pm.State(lambda old: (x ** y, old + 1))

# ------------------------------------------------------------------------------
# Test class implementations
# ------------------------------------------------------------------------------


class Functor(pm.Functor):
    def fmap(self, *args):
        pass


class Applicative(pm.Applicative):
    def fmap(self, *args):
        pass

    def amap(self, *args):
        pass


class Monad(pm.Monad):
    def bind(self, *args):
        pass

    def fmap(self, *args):
        pass

    def amap(self, *args):
        pass


if DEBUG:
    with Section('Functional programming with PyMonad'):
        # Partial Applications
        # Curried vs. non-curried
        print_h2('Partial Applications')
        assert add2(2, 3) == add2(2)(3)
        assert add3(2, 3, 4) == add3(2, 3)(4)
        add_to_5 = add3(2, 3)
        print(add_to_5(10))  # 15
        # Partially applied thrice
        assert add3(1)(2)(3) == add3(1, 2, 3)

        # Compositions
        print_h2('Compositions')
        composed = add * sub2
        # Add numbers (2), then subtract 2, as the function composition entails.
        assert composed(1, 1) == 0
        # Composed and partially applied.
        comp_partial = add2(2) * add3(2, 3)
        print(comp_partial(2))

        # Functors
        print_h2('Functors')
        print(neg * pm.List(*range(10)))
        print(neg * pm.Just(0))
        print(neg * pm.Nothing)  # Bottom type?

        nums = sub2 * pm.List(*range(10))
        print(nums)
        # Functor + partial application and composition
        nums2 = comp_partial * pm.List(*range(4))
        print(nums2)

        # List comprehension of sub-lists from Functor with partial
        # application and composition of outer Functor list
        ppr([sub2 * pm.List(
            *range(n)) for n in comp_partial * pm.List(*nums2)])

        # Bind functor and curried function and then re-compose with new values
        print_h2('Applicative functors')
        bound = add2 * pm.List(*range(3)) & pm.List(*range(3))
        ppr([bound, neg * bound])
        # Playing around
        f = map(lambda x: pm.List(range(x)), range(10))
        ppr(f)

        f = add * monoid_range(4) & monoid_range(2)
        print(f)
        print(neg * f)

        # Bind all once
        print_h2('Applicative functors, partial applications and compositions')
        bound1 = add2 * pm.List(*range(2)) & pm.List(*range(2))
        # Bind all a second time
        bound2 = add_ten_to * pm.List(*range(2)) & bound1
        ppr(bound2)

        ppr(num_and_ranges(10))

        assert negafy(*range(10)) == neg * monoid_range(10)

        # Combining Functors * 4
        names = pm.List(*[random_person()['name'] for _ in range(4)])
        f1 = foofix * names
        f2 = foofix * f1
        f3 = foofix * f2
        f4 = foofix * f3
        print(f1)
        print(f2)
        print(f3)
        print(f4)
        assert f4[0].startswith('FOO_FOO_FOO_FOO_')

        print_h2('Monads')
        f = monoid_range(4) >> monoid_range(4)
        ppr(neg * f)

        print(pm.Just(9) >> pm.Just(10))
        print(monoid_range(3))

        f = monoid_range(5) >> sqr >> exp(2)
        ppr(f)

        print_h2('Custom Functors, Monads and Applicative Functors')

        # ---------

        print_h2('Custom State Monad')
        state1 = pm.unit(pm.State, 1) >> s_add(3) >> s_exp(10) >> s_sub(3)
        state2 = pm.unit(pm.State, 1) >> s_add(10) >> s_exp(2) >> s_sub(100)
        print(state1(4))
        print(state2(4))
