"""Module docstring.

This talks about the module."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class MyClass(object):
    """Class docstring."""

    raise NotImplementedError


if DEBUG:
    with Section('SOME MODULE TITLE'):
        pass
