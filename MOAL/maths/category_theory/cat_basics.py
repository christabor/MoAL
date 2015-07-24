# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h4
from MOAL.helpers.display import print_simple
from MOAL.helpers.datamaker import random_dna
from functools import wraps

DEBUG = True if __name__ == '__main__' else False


def annotate(func, *args, **kwargs):
    """A decorate to annotate with the function name when it's called."""
    @wraps(func)
    def _inner(*args, **kwargs):
        print('Calling function: "{}"'.format(func.__name__))
        return func(*args, **kwargs)
    return _inner


@annotate
def dictify(arg):
    """Convert arg to a dict.

    Args:
        arg (mixed) - the thing to convert to a dictionary.
    """
    return {'arg': arg}


@annotate
def listify(arg):
    """Convert arg to a list.

    Args:
        arg (mixed) - the thing to convert to a list.
    """
    return [arg]


def fooify(thing):
    return 'FOO_{}'.format(thing)


def bazify(thing):
    return '{}_BAZ'.format(thing)


def prefix(thing, prefix='_:'):
    return '{}{}'.format(prefix, thing)


def delimit(thing, delimiter=','):
    return '{}{}'.format(thing, delimiter)


def compose_hybrid(arg, **kwargs):
    f = kwargs.get('f')
    g = kwargs.get('g')
    return f(g(arg))


def compose_hybrid_hof(**kwargs):
    f = kwargs.get('f')
    g = kwargs.get('g')

    def _compose(*args, **kwargs):
        return f(g(*args, **kwargs))
    return _compose


def id(thing):
    """Identity function.

    Args:
        thing (mixed) - the thing to return.
    """
    return thing

"""Closer to canonical functions."""


def f(a):
    return a ** a


def g(b):
    return b * 2


def f_g(a, b, arg):
    return a(b(arg))


if DEBUG:
    with Section('Category Theory basics'):
        """Challenge ideas taken from bartoszmilewski.com/2014/11/04
            /category-the-essence-of-composition/ "Challenges" section."""
        print_h4('Identity function')
        for thing in ['cat', 1, 'dog', 2, range(0, 3), 0.03]:
            assert thing == id(thing)
            print(thing, id(thing))
        print_h4('Function composition')
        res = compose_hybrid('composition is neat!', f=dictify, g=listify)
        print(res)
        print_h4('Random funcs')
        print(listify('foo'))
        print(dictify('foo'))

        print_h4('Higher order function composition')
        f2 = compose_hybrid_hof(f=listify, g=dictify)
        print(f2('composition yay!'))

        print_h4('Function composition on a "stream" or incoming set')
        res = [compose_hybrid(str(x), f=fooify, g=bazify) for x in range(4)]
        print(res)
        print_h4('Messing around...')
        res = ''.join(res)
        for x in range(4):
            res += compose_hybrid(x, f=fooify, g=bazify)
        print(res)
        res = ''
        for x in range(10):
            # Just to make things interesting...
            res += compose_hybrid(random_dna(), f=delimit, g=prefix)
        print(res)

        composed = f_g(f, g, 4)
        print_simple('Traditional composed example:', composed, newline=False)
