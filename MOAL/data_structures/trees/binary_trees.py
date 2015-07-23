# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h4
from MOAL.helpers.display import cmd_title
from MOAL.data_structures.abstract.tree import Tree

DEBUG = True if __name__ == '__main__' else False


class InvalidChildNodeCount(Exception):
    pass


class BinaryTree(Tree):
    """A binary tree is the same as a tree ADT, except each node must have a max
    of two child nodes, unless it's a leaf node, in which case it has zero."""

    def __setitem__(self, key, val):
        if len(val['edges']) > 2:
            raise InvalidChildNodeCount(
                'Binary Tree cannot have more than two children!')
        super(BinaryTree, self).__setitem__(key, val)

    def is_degenerate(self):
        pass

    def is_pathological(self):
        return self.is_degenerate()


class BifurcatingArborescence(BinaryTree):
    """A hilariously verbose alternative name for a Binary Tree!"""


if DEBUG:
    with Section('Binary Tree'):
        """
                            0  root
                           / \
                          /   \
                         1     2  interior
                        /     / \
                       /     /   \
                      3     4     5  leaves

          The tree above is represented in python code below.

        """
        btree = BinaryTree({
            0: {'edges': [1, 2], 'is_root': True},
            1: {'edges': [3], 'parent': 0},
            2: {'edges': [4, 5], 'parent': 0},
            3: {'edges': [], 'parent': 1},
            4: {'edges': [], 'parent': 2},
            5: {'edges': [], 'parent': 2},
        })
        print(btree)

        print_h4(
            'Binary trees',
            desc=('They can have no more than two nodes, '
                  'so adding new edges that do not conform'
                  ' should throw an error.'))
        try:
            btree[6] = {'edges': [7, 8, 9], 'parent': 3}
        except ValueError:
            cmd_title('Error called successfully', newlines=False)
