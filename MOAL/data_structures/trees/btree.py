# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.data_structures.abstract.tree import Tree

DEBUG = True if __name__ == '__main__' else False


class InvalidNodeKeys(Exception):
    pass


class BTree(Tree):
    def __setitem__(self, key, node):
        """Require keys as per the Btree specification.
        Note: keys are not checked for validity as integer values,
        merely that they exist."""
        if 'keys' not in node:
            raise InvalidNodeKeys('Each node must have a keys list')
        edges = len(node['edges'])
        # Each node must have a number of keys totalling
        # 1 less than it's total children.
        if len(node['keys']) != edges - 1 and edges > 1:
            raise InvalidNodeKeys(
                'Each node must have keys totalling 1 less'
                ' than the total children keys')
        return super(Tree, self).__setitem__(key, node)

    def __str__(self):
        display = []
        for vertex, data in self.vertices.iteritems():
            f = '({vertex}) --> {outbound}'.format(
                vertex=vertex, outbound=data['edges'])
            f += '\n |______<{}>\n'.format(data['keys'])
            display.append(f)
        return '\n'.join(display)

    def get_keys(self, node_name):
        return self.__getitem__(node_name).get('keys')

    def add_key(self, node_name, key):
        node = self.__getitem__(node_name)
        node['keys'].append(key)


if DEBUG:
    with Section('BTree Trees'):
        graph = {
            0: {'edges': [1], 'is_root': True, 'keys': ['A', 'B', 'C']},
            1: {'edges': [2, 3], 'parent': 0, 'keys': ['D']},
            2: {'edges': [4, 5, 6], 'parent': 1, 'keys': ['E', 'F']},
            3: {'edges': [], 'keys': ['G']},
            4: {'edges': [], 'keys': ['H']},
            5: {'edges': [], 'keys': ['I']},
            6: {'edges': [], 'keys': ['J']},
        }
        btree = BTree(graph)
        assert btree.get_keys(2) == ['E', 'F']
        btree.add_key(4, {'key': 'Z'})
        print(btree)
        assert btree.get_keys(4) == ['H', {'key': 'Z'}]
