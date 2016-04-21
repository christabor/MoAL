"""A basic implementation of a pushdown stack,
using a subclassed Python list."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

IS_MAIN = True if __name__ == '__main__' else False

if IS_MAIN:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

import operator

from MOAL.helpers.display import Section


class StackMachine(list):

    def __init__(self, *args, **kwargs):
        super(StackMachine, self).__init__(*args, **kwargs)

    def __str__(self):
        return '\n'.join(self)

    def _from_operator(self, token):
        if token == '/':
            return 'divide'
        elif token == '*':
            return 'multiply'
        elif token == '+':
            return 'add'
        elif token == '-':
            return 'subtract'
        else:
            return 'push {}'.format(token)

    def _to_operator(self, token):
        if token == 'divide':
            return operator.div
        elif token == 'multiply':
            return operator.mul
        elif token == 'add':
            return operator.add
        elif token == 'subtract':
            return operator.sub

    def evaluate(self):
        """Evaluate items on the stack.

        In this case, it should only be the first three items:
            [operand, operand, operator].
        """
        operand1, operand2, operator = (
            int(self.pop().replace('push ', '')),
            int(self.pop().replace('push ', '')),
            self._to_operator(self.pop()),
        )
        res = operator(operand1, operand2)
        print('evaluation result = {}'.format(res))
        return res

    def append(self, val):
        """Add an item to stack.

        Expressions are tokenized and then sorted so the operands are the first
        two indices, which are evaluated ala prefix notation using LIFO.
        """
        # sub = []
        try:
            vals = val.split(' ')
        except AttributeError:
            return
        for token in vals:
            try:
                token = 'push {}'.format(int(token))
                super(StackMachine, self).append(token)
            except ValueError:
                super(StackMachine, self).insert(
                    0, self._from_operator(token))

if IS_MAIN:
    with Section('Pushdown stack'):
        exprs = [
            (5, '2 + 3'),
            (3, '3 * 1'),
            (999, '0 + 999'),
            (1000, '10 * 100'),
            (-1000, '-10 * 100'),
            (0, '0 * 1'),
            (1, '1 / 1'),
            (10, '1 / 10'),
            (0, '10 / 2'),
            (5, '2 / 10'),
        ]

        smachine = StackMachine()

        for item in exprs:
            expected, expr = item
            smachine.append(expr)
            res = smachine.evaluate()
            print('Expected {}, Res = {}'.format(expected, res))
            assert expected == res

        print(smachine)
