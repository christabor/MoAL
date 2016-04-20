"""Module docstring. This talks about the module."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

IS_MAIN = True if __name__ == '__main__' else False

if IS_MAIN:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section


class MyClass(object):
    """Class docstring."""

    raise NotImplementedError


if IS_MAIN:
    with Section('SOME MODULE TITLE'):
        pass
