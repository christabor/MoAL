# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import divider
from functools import wraps

DEBUG = True if __name__ == '__main__' else False


def returns(retval=None):
    """Check the specified return type with the functions return value to
    make sure that its type matches."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _retval = func(*args, **kwargs)
            assert isinstance(_retval, retval)
        return wrapper
    return decorator


def types(*args_types, **kwargs_types):
    """Loop over all args and kwargs passed to the function and check
    the corresponding types to make sure they all match."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check kwargs
            for k, v in kwargs.iteritems():
                assert isinstance(v, kwargs_types[k])
            # Check args
            for i, arg in enumerate(args):
                # Check if it's an *args situation, versus specified types.
                # If so, then use the single specified argument
                # for all *args here.
                assert isinstance(arg, args_types[i])
            func(*args, **kwargs)
        return wrapper
    return decorator


@types(str, str, three=str, four=str)
@returns(retval=str)
def concat(one, two, three='', four=''):
    return '{}{}'.format(one, two)


@types(int, int)
@returns(retval=int)
def add2(one, two):
    return one + two


@types(dict, dict)
@returns(retval=dict)
def combine_dict(dict1, dict2):
    dict1.update(**dict2)
    return dict1


@returns(retval=list)
def combine_lists(*args):
    f = []
    for l in args:
        f += l
    return f


@returns(retval=long)
def sum_square(*nums):
    f = 0
    for n in nums:
        f += n ** n
    return f


if DEBUG:
    with Section('Type checking via python decorators!'):
        # Correct types
        concat('cat', 'dog')
        add2(1, 2)
        combine_dict({'dog': 1, 'cat': 1}, {'cat': 0})
        combine_lists([1, 2, 3], [2, 3], [40, 30, 20, 10])
        sum_square(*range(1, 100))

        print('Type checking worked!')
        divider()
        # Incorrect types
        try:
            concat('cat', 0)
        except AssertionError:
            print('Type checking worked with failure!')

        try:
            add2(1, None)
        except AssertionError:
            print('Type checking worked with failure!')

        try:
            combine_dict({}, None)
        except AssertionError:
            print('Type checking worked with failure!')
