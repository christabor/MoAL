# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.data_structures.trees import binary_search_trees as bst

DEBUG = True if __name__ == '__main__' else False


class OrderStatisticBST(bst.BinarySearchTree):
    """
    [From Wikipedia]

        "In computer science, an order statistic tree is a variant of the binary
        search tree, that supports two additional operations beyond
        insertion, lookup and deletion:

        * Select(i) - find the 'i'th' smallest element stored in the tree

        * Rank(x) - find the rank of element x in the tree, i.e. its index in
            the sorted list of elements of the tree

        Both operations can be performed in O(log n) time in the average case;
        when a self-balancing tree is used as the base data structure,
        this bound also applies in the worst case."
    """

    def _put(self, *args):
        """Override default behavior to augment size property."""
        current = super(OrderStatisticBST, self)._put(*args)
        count = 0
        while current.has_left_child():
            current = current.left_child
            count += 1
        current.size = count

    def select(self, size):
        for node in self:
            if node.size == size:
                return node

    def rank(self, node):
        ranked = []
        for _node in self:
            ranked.append((_node, _node.size))
        # Sort by size, but leave node reference intact.
        for data in ranked:
            _node, size = data
            if _node.name == node:
                return size


if DEBUG:
    with Section('Order statistic - Binary Search Tree'):
        stats_bst = OrderStatisticBST()
        # Create a reasonable spread out tree
        for x in range(1, 6):
            stats_bst.put(x * x, {'num': x * x})
            stats_bst.put(x * 20, {'num': x * 20})
        bst.recurse_bst(stats_bst.root, None)

        print(stats_bst[1].data)
        print(stats_bst[100].data)

        print_h2('Testing select function')
        for n in range(10):
            print(stats_bst.select(n))

        print_h2('Testing rank function')
        for n in range(10):
            print(stats_bst.rank(n))
