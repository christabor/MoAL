"""
The UNIX Rule of Transparency.

See http://www.catb.org/esr/writings/taoup/html/ch01s06.html for more.
"""
# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from random import choice
import pdb
import sys

DEBUG = True if __name__ == '__main__' else False
# Allow debugging from command line.
DEBUG_PDB = '--debug' in sys.argv


# Not transparent - BAD
def gnrt_rndm_nms(cnt):
    f = ['Jane', 'Hans', 'Ella', 'Lois', 'Bernardo', 'Yolanda']
    l = ['McKinley', 'Adams', 'Salvatore', 'Geoffries', 'Fritzmann', 'Smith']
    return ['{} {}'.format(choice(f), choice(l)) for val in range(cnt)]


# Transparent - GOOD
# It has the following transparent properties:
#   1. Docstrings, for reader and for introspection
#   2. Arguments/returns values
#   3. Default value, with a sensible default, keyword argument based.
#   4. Type checking.
#   5. Easy to understand varaible names and method name.
def get_random_names(count=3):
    """Get a list of random first and last names, up to `count`.

    Args:
        count (int, optional): The number of names to generate. Default is 3.
    Returns:
        names (list): The list of generated names.
    """
    if not isinstance(count, int):
        raise ValueError('Need a number!')
    first_names = ['Jane', 'Hans', 'Ella', 'Lois', 'Bernardo', 'Yolanda']
    last_names = [
        'McKinley', 'Adams', 'Salvatore', 'Geoffries', 'Fritzmann', 'Smith']
    return ['{} {}'.format(
        choice(first_names), choice(last_names)) for _ in range(count)]


if DEBUG_PDB:
    pdb.set_trace()
    print(get_random_names(count=3))
