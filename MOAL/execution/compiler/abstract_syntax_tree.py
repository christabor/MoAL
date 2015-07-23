# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_h2
from helpers.display import print_info
import inspect
import ast

DEBUG = True if __name__ == '__main__' else False


def foo():
    """Foo is a function that creates a range of ranges that increases
    by multiplying i + 1 each time, from 1 to 100, then sums the sum of each
    range and prints it."""
    f = [range(i, i * 100 + i) for i in range(1, 10)]
    res = sum(sum(r) for r in f)
    print('Result is: {}'.format(res))


def bar():
    """Bar is a function that creates a range of ranges that increases
    by adding i + 1 each time, from 1 to 100, then sums the sum of each
    range and prints it."""
    f = [range(i, i + 100 + i) for i in range(1, 10)]
    res = sum(sum(r) for r in f)
    print('Result is: {}'.format(res))


def ast_drawing():
    """The AST Drawing.

    unaryOp = `-1`

        (ROOT)
         / \
       [-] [1]

    binaryOp = `2 + 2`

        (ROOT)
         /
       [+]
       / \
     [2] [2]

    etc... `foo = 3 * 9`

        (ROOT)
         /  \
       [=]  [*]
       /    /  \
     [foo] [3] [9]

    """

if DEBUG:
    with Section('Abstract Syntax Tree (AST)'):
        print_h2('Reading functions and then building ast and executing.')
        src1 = inspect.getsource(foo)
        src2 = inspect.getsource(bar)
        tree = ast.parse(src1 + '\nfoo()\n' + src2 + '\nbar()')
        print_info(tree)
        exec(compile(tree, filename='<ast>', mode='exec'))

        drawing = ast.parse(inspect.getsource(ast_drawing), filename='<ast>')
        print_info('Printing AST docstring, a drawing of an AST (such meta)')
        for node in ast.walk(drawing):
            try:
                print(ast.get_docstring(node))
            except TypeError:
                continue
