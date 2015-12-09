# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.data_structures.trees.btree import BTree
from MOAL.data_structures.abstract.tree import Tree

DEBUG = True if __name__ == '__main__' else False


class InvalidNodeCount(Exception):
    pass


class TwoThreeFourTree(BTree):
    """From Wikipedia:
    "The numbers mean a tree where every node with children (internal node)
    has either two, three, or four child nodes:
    a 2-node has one data element, and if internal has two child nodes;
    a 3-node has two data elements, and if internal has three child nodes;
    a 4-node has three data elements, and if internal has four child nodes."

    Here, "N-node" is determined by the count of `keys` in a node.
    """

    def __setitem__(self, key, node):
        valid = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        keys_nodes = (len(node['edges']), len(node['keys']))
        if keys_nodes not in valid:
            print(node)
            raise InvalidNodeCount(
                '{} is not a valid number of nodes/keys. '
                'Must be one of: {}.'.format(keys_nodes, valid))
        # The BTree requirements conflict with the 2,3,4 tree requirements
        # so we use the abstract tree for getting/setting overrides.
        return super(Tree, self).__setitem__(key, node)


if DEBUG:
    with Section('2, 3, 4 Tree'):
        """
                       0 root
                      /
                     1
                    / \
               ___ 2   3
              /   / \
             4   5   6

          The tree above is represented in python code below.

        """

        graph = {
            0: {'edges': [1], 'is_root': True, 'keys': ['A']},
            1: {'edges': [2, 3], 'parent': 0, 'keys': ['B', 'C']},
            2: {'edges': [4, 5, 6], 'parent': 1, 'keys': ['C', 'Z', 'E']},
            3: {'edges': [], 'keys': []},
            4: {'edges': [], 'keys': []},
            5: {'edges': [], 'keys': []},
            6: {'edges': [], 'keys': []},
        }

        two34 = TwoThreeFourTree(graph)
        assert not two34.is_leaf(99)
        assert not two34.is_internal(99)
        assert two34.is_internal(2)
        assert two34.is_leaf(4)
