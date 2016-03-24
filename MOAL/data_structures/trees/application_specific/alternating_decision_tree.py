# -*- coding: utf-8 -*-

"""Alternating decision tree.
See https://en.wikipedia.org/wiki/Alternating_decision_tree for more.

'An alternating decision tree (ADTree) is a machine learning method for
classification. It generalizes decision trees and has connections to boosting.

An ADTree consists of an alternation of decision nodes,
which specify a predicate condition, and prediction nodes,
which contain a single number.

An instance is classified by an ADTree by following all paths
for which all decision nodes are true, and summing
any prediction nodes that are traversed.'
"""

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


from MOAL.data_structures.abstract.tree import Tree
from MOAL.helpers.display import Section
from MOAL.helpers.display import cmd_title
from MOAL.helpers.display import divider


class AlternatingDecisionTree(Tree):

    def __init__(self, *args, **kwargs):
        super(AlternatingDecisionTree, self).__init__(*args, **kwargs)
        self.default_vals = {'func': self._noop, 'next': [0, 0]}
        # Make sure all nodes have default boolean paths on them.
        for k, v in self.vertices.items():
            if 'fork' not in self.vertices[k]:
                self.vertices[k]['fork'] = self.default_vals

    def _noop(self, *args, **kwargs):
        pass

    def add_rule(self, key, func, next_conditions):
        """Add a rule to the tree.

        This will map an evaluation function to a specific node and
        a left or right branch.
        """
        if key not in self.vertices:
            raise ValueError('Invalid key: {}'.format(key))
        self.vertices[key]['fork'] = {
            'next': next_conditions,
            'func': func
        }

    def evaluate(self, value, fromkey=None):
        """Evaluate a value against the tree.

        Evaluations start from the top if no fromkey is specified.
        A sum is returned for the total of all resulting path evaluations."""
        total = 0

        def _eval(node):
            print('func', node['func'](value))
            res = node['func'](value)
            # Update based on evaluation function results.
            path = 0 if res else 1
            total = node['next'][path]
            print('took path: {} with val {}'.format(path, value))
            return total

        for k, v in self.vertices.items():
            divider()
            cmd_title('NODE: {}'.format(k))
            node = self.vertices[k]['fork']
            if fromkey is not None:
                if k == fromkey:
                    total += _eval(node)
                    print('new total: ', total)
                else:
                    continue
            else:
                total += _eval(node)
                print('new total: ', total)
        print('FINAL value ', total)

    def predict(self, value, fromkey=None):
        return self.evaluate(value, fromkey=fromkey)


def is_lt_10(val):
    """Test evaluation function."""
    print('Calling is_lt_10 with ', val)
    return val < 10


def is_gt_10(val):
    """Test evaluation function."""
    print('Calling is_gt_10 with ', val)
    return val > 10


def isodd(val):
    """Test evaluation function."""
    print('Calling isodd with', val)
    return val % 2 != 0


def iseven(val):
    """Test evaluation function."""
    print('Calling iseven with', val)
    return val % 2 == 0


if DEBUG:
    with Section('Alternating Decision Tree'):
        adt = AlternatingDecisionTree({
            0: {'edges': [1, 2, 3, 4], 'is_root': True},
            1: {'edges': [], 'parent': 0},
            2: {'edges': [5], 'parent': 0},
            3: {'edges': [6], 'parent': 0},
            4: {'edges': [], 'parent': 0},
            5: {'edges': [], 'parent': 2},
            6: {'edges': [], 'parent': 3},
        })

        adt.add_rule(1, is_gt_10, [0.1, 0.4])
        adt.add_rule(2, is_gt_10, [3.1, 0.4])
        adt.add_rule(3, iseven, [2.0, 10])
        adt.add_rule(4, isodd, [12.0, 10])
        adt.evaluate(20)
