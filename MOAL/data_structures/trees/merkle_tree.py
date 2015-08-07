# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.data_structures.hashes.hashtable import NaiveHashTable
from MOAL.data_structures.trees.binary_trees import BinaryTree
from MOAL.data_structures.abstract.tree import Tree
import tiger

DEBUG = True if __name__ == '__main__' else False


class MerkleTree(Tree, NaiveHashTable):
    """From Wikipedia: "In cryptography and computer science,
    a hash tree or Merkle tree is a tree in which every non-leaf node is
    labeled with the hash of the labels of its children nodes."
    """

    def _hash(self, data):
        """Defer to generic hash name to make simplified overrides easy."""
        return self.hash_fnv1(data)

    def __setitem__(self, key, node):
        child_data = ''
        if 'is_leaf' not in node:
            child_data = [self[c]['val'] for c
                          in node['edges'] if 'val' in self[c]]
        node['val'] = sum([self._hash(c) for c in child_data])
        super(MerkleTree, self).__setitem__(key, node)

    def get_children(self, node_name):
        return self.__getitem__(node_name).get('edges')


class TigerTreeHash(BinaryTree, MerkleTree):
    """From Wikipedia:
    "The Tiger tree hash is a widely used form of hash tree. It uses a binary
    hash tree (two child nodes under each node), usually has a data block size
    of 1024-bytes and uses the cryptographically secure Tiger hash."
    """

    def _hash(self, data):
        return tiger.new(data).hexdigest()


if DEBUG:
    with Section('Hashed array tree'):
        merkle = MerkleTree({
            0: {'edges': [1, 2, 3], 'is_root': True},
            1: {'edges': [], 'parent': 0, 'val': 'Foobar'},
            2: {'edges': [4], 'parent': 0, 'val': 'Foobar'},
            3: {'edges': [5], 'parent': 0, 'val': 'Foobar'},
            4: {'edges': [], 'parent': 0, 'val': 'Foobar'},
            5: {'edges': [], 'parent': 0, 'val': 'Foobar'},
        })
        for k, node in merkle.vertices.iteritems():
            print('Node edges: {}, Child hash: {}'.format(
                node['edges'], node['val']))
