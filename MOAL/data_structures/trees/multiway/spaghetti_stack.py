# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class InvalidNode(Exception):
    pass


class SpaghettiStack:
    """From Wikipedia:
    "In computer science, an in-tree or parent pointer tree is an N-ary tree
    data structure in which each node has a pointer to its parent node,
    but no pointers to child nodes."
    """

    def __init__(self):
        self.leaves = []

    def add(self, leaves):
        self.leaves += leaves

    def __str__(self):
        print('[root]')
        for leaf in self.leaves:
            c = 0
            res = []
            while leaf.next is not None:
                string = '{}{}'.format(' ' * c, leaf.key)
                res.append(string)
                c += 1
                leaf = leaf.next

            for r in reversed(res):
                print(r)
            print('=================')
        return ''


class SpaghettiNode:
    def __init__(self, key):
        self.key = key
        self.next = None


if DEBUG:
    with Section('BTree Trees'):
        """
            0
            |
            1
            |
            2
           / \
          3   4
         / \   \
        5   6   7
        |   |   |
        8   9   10
        |
        11

          The tree above is represented in python code below.
        """
        spag = SpaghettiStack()

        intnode3 = SpaghettiNode('3')
        intnode2 = SpaghettiNode('2')

        leaf11 = SpaghettiNode('11')
        leaf11.next = SpaghettiNode('8')
        leaf11.next.next = SpaghettiNode('5')
        leaf11.next.next.next = intnode3
        leaf11.next.next.next.next = intnode2
        leaf11.next.next.next.next.next = SpaghettiNode('1')
        leaf11.next.next.next.next.next.next = SpaghettiNode('0')

        leaf9 = SpaghettiNode('9')
        leaf9.next = SpaghettiNode('6')
        leaf9.next.next = intnode3

        leaf10 = SpaghettiNode('10')
        leaf10.next = SpaghettiNode('7')
        leaf10.next.next = SpaghettiNode('4')
        leaf10.next.next.next = intnode2

        spag.add([leaf11, leaf10, leaf9])
        print(spag)
