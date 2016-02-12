"""
The UNIX Rule of Silence.

See http://www.linfo.org/rule_of_silence.html for more.

Ironically, MOAL has plenty of non-silent debugging code,
but most of the time it is hidden behind an `if DEBUG` flag,
which is one way to go about it.

Another argument is that debug code (except logging) should not even live in
source control, and should be removed before being committed
(e.g. using git pre-commit hooks to search for the `print` statement.)
"""
# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


# Not silent - BAD
def concat(strs):
    """Add some strs together."""
    string = ''
    for val in strs:
        print('--- Current val: {}'.format(val))
        string += val
    print('Concatenating val!')
    return string


# Silent, except for errors - GOOD
def concat2(strs):
    """Add some strs together - silently."""
    string = ''
    for val in strs:
        if not isinstance(val, str):
            raise ValueError('Invalid string!')
        string += '{}'.format(val)
    return string


if DEBUG:
    with Section('UNIX Rule of Silence'):
        print(concat(['cat', 'dog', 'banana', 'goat']))
        print(concat2(['cat', 'dog', 'banana', 'goat', 3]))
