"""Referential transparency examples."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

IS_MAIN = True if __name__ == '__main__' else False

if IS_MAIN:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from random import randrange
import os

from MOAL.helpers.display import Section

some_currval = 2


def func1():
    """RT func."""
    return 2


def func2():
    """Non-RT func."""
    return randrange(0, 10000)


def func3():
    """Non-RT func."""
    global some_currval
    some_currval += 1
    return some_currval


def func4(name):
    """RT func."""
    return 'Hello {name}'.format(name=name)


def func5(name):
    """RT func, using another RT func in a different context."""
    return func4(name)


def func6(name):
    """RT func, using other RT funcs in a different context."""
    return func4(name), func1(), func5(name)


def func7(name):
    """RT func, using other RT funcs in a different context - nested tests."""
    assert func5(name) == func5(name) == func5(name)
    return func4(name), func1(), func5(name)


if IS_MAIN:
    with Section('Referential transparency'):
        username = os.getuid()
        assert func1() == func1() == func1()
        # Non-deterministically non-referentially transparent
        assert func2() != func2() != func2()
        # Deterministically non-referentially transparent
        assert func3() != func3() != func3()

        assert func4(username) == func4(username) == func4(username)
        assert func5(username) == func5(username) == func5(username)
        assert func6(username) == func6(username) == func6(username)
        assert func7(username) == func7(username) == func7(username)
