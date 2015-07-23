# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import prnt
from MOAL.helpers.display import print_simple
from symtable import symtable

DEBUG = True if __name__ == '__main__' else False


test_func = """
class Words:
    def concat(self, x, y):
        return '{}{}'.format(x, y)

class Maths:
    def add_squared(self, x, y):
        return x ** 2 + y **2

"""

example_output = """
----------------------------
Name        | Type
----------------------------
Words       | class
concat      | def
self        | def var
x           | def var
y           | def var
'{}{}'      | string object
----------------------------

----------------------------
Name        | Type
----------------------------
Maths       | class
add_squared | def
self        | def var
x           | def var
y           | def var
'{}{}'      | string object
2           | integer
----------------------------
"""


def format_table(code_string):
    s_table = symtable(code_string, 'string', 'exec')
    table = []
    for child in s_table.get_children():
        row = {
            'name': child.get_name(),
            'scope': 'global',
            'children': [subchild.get_name() for subchild
                         in child.get_children()]
        }
        table.append(row)
    return s_table, table


if DEBUG:
    with Section('Data structure - symbol table'):
        """Messing around with built-in symbol table parser."""
        prnt('Some example code...', test_func)
        symbols, formatted = format_table(test_func)
        assert len(symbols.lookup('Maths').get_namespaces()) == 1
        assert len(symbols.lookup('Words').get_namespaces()) == 1

        print_simple(
            'Output using stdlib symtable module:', [symbols, formatted])
        prnt('Which might be translated to...', example_output)
