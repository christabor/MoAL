# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import prnt
from MOAL.helpers import adts as test_module
import inspect as insp

DEBUG = True if __name__ == '__main__' else False


def suggest_errors(name, func):
    print_h2('Suggestions for: {}'.format(name))
    args, varargs, keywords, defaults = insp.getargspec(func)
    prnt('Args:', args)
    prnt('VarArgs:', varargs)
    prnt('Kwargs:', keywords)
    prnt('Defaults:', '')

    if defaults is not None:
        for val in defaults:
            if isinstance(val, int):
                print('Default val "{}" is an int; '
                      'have you tried testing a float?'.format(val))
            if isinstance(val, float):
                print('Default val "{}" is an float; '
                      'have you tried testing an int?'.format(val))
            if isinstance(val, str):
                print('Default val "{}" is a str; '
                      'have you tried testing a string? or None?'.format(val))
            if isinstance(val, list):
                print('Default val "{}" is a list; '
                      'have you tried testing empty? '
                      'full of values? with a dictionary?'.format(val))
            if isinstance(val, dict):
                print('Default val "{}" is a dict; '
                      'have you tried testing empty? '
                      'full of values? with a list? '
                      'with bad keys'.format(val))
            if isinstance(val, bool):
                print('Default val "{}" is a bool; have you tried the '
                      'opposite ({})?'.format(val, not val))


def pred_get_valid_funcs(data):
    name, func = data
    if insp.isclass(func):
        return False
    if hasattr(func, 'im_self'):
        return False
    if not name.startswith('__') and callable(func):
        return True
    return False


if DEBUG:
    with Section('Error guessing'):
        funcs = filter(pred_get_valid_funcs, insp.getmembers(test_module))
        for func in funcs:
            suggest_errors(*func)
