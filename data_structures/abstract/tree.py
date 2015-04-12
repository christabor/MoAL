# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from helpers.display import print_h2
from helpers.display import print_h4
from helpers.display import print_error
from helpers.display import print_table
from helpers.display import divider
from helpers.display import cmd_title
from helpers.display import uncase_snake_upper
from Queue import Queue as StdQueue
from data_structures.graphs.graphs import Graph
from data_structures.abstract.queues import Queue
from collections import OrderedDict
import time


DEBUG = True if __name__ == '__main__' else False


class InvalidGraph(Exception):
    pass


class InvalidNode(Exception):
    pass


class Tree(Graph):
    """This implementation is completely abstract, and allows for an
    N-ary tree (e.g. there can be N child, sibling or parent nodes).

    More concrete trees with specified properties or requirements will be
    sub-classed from this one. The graph created before this has been used,
    since it is even more abstract, and has many of the useful
    properties and methods we want.

    Terms implemented as methods and/or properties:
    (en.wikipedia.org/wiki/Tree_(data_structure))
    """

    def __init__(self, vertices={}):
        super(Tree, self).__init__(vertices=vertices)
        # Add all given vertices
        for key, node in vertices.iteritems():
            self.__setitem__(key, node)

    def path(self, start_node, end_node):
        """From Wikipedia:
        "Path: a sequence of nodes and edges connecting
        a node with a descendant." """
        return super(Tree, self).walk(start_node, end_node)

    def level(self, node_name):
        # Level: The level of a node is defined by 1 + the number of
        #     connections between the node and the root.
        raise NotImplementedError

    def __delitem__(self, key):
        edges = self.__getitem__(key).get('edges')
        # Delete children
        for edge in edges:
            del self.vertices[edge]
            self.node_count -= 1
        # Delete node
        del self.vertices[key]
        self.node_count -= 1

    def __getitem__(self, key):
        node = super(Tree, self).__getitem__(key)
        return node

    def __setitem__(self, key, val):
        node = super(Tree, self).__setitem__(key, val)
        # Set root to False if not specified, otherwise True
        node.update({'is_root': node.get('is_root', False)})
        node.update({'is_child': not node.get('is_root', True)})
        node.update({'edges': node.get('edges', [])})
        is_leaf = len(node.get('edges')) == 0
        node.update({'is_leaf': is_leaf})
        node.update({'parent': node.get('parent', None)})
        return node

    def node_depth(self, node_name, use_root=False):
        """Determine the depth of a node - which is the number of nodes
        between this node and the root (going up, the opposite of node_height).
        If `use_root` is set, just returns 1, since the root has a depth of 1"""
        height = 1
        if use_root:
            return height
        node = self.__getitem__(node_name)
        while not node.get('is_root'):
            height += 1
            node = self.__getitem__(node.get('parent'))
        return height

    def node_height(self, node_name, height=1, use_root=False):
        """Determine the height of a node - which is the number of nodes
        between this node and a terminal (leaf) node. If `use_root` is set,
        gets the height starting from the very top."""
        node = self.get_root() if use_root else self.__getitem__(node_name)
        if node.get('is_leaf'):
            return height
        for child_name in node.get('edges'):
            return self.node_height(child_name, height=height + 1)
        return height

    def total_height(self):
        """Similar to height, but height is always absolute, rather than
        relative from a specific node; also hides the details behind
        a simpler interface with no arguments."""
        return self.node_height(None, use_root=True)

    def get_siblings(self, node_name):
        """Return all siblings `node_name`, derived from its parent edges."""
        node = self.__getitem__(node_name)
        return self.__getitem__(node.get('parent')).get('edges')

    def is_descendant(self, node_name, descendant_name):
        """Determine if the given node is a descendant (below) of this node."""

        return self.node_height(node_name) < self.node_height(descendant_name)

    def is_ancestor(self, ancestor_name, node_name):
        """Determine if the given node is an ancestor (above) of this node."""
        return self.node_depth(ancestor_name) < self.node_depth(node_name)

    def get_root(self):
        """Moves up to the root of the tree from current position."""
        for key, node in self.vertices.iteritems():
            if node.get('is_root'):
                return node
        # If we couldn't go up, then no root was specified, or the
        # edges are invalid, so raise an error.
        raise InvalidGraph

    def has_children(self, node_name):
        """Return True or False, depending on whether the node has children."""
        return len(self.__getitem__(node_name)['edges']) > 0

    def has_sibling(self, node_name, sibling_name=None, cached=None):
        """Return True if node_name shares the same parent as this node,
        otherwise returns False."""
        node = cached if cached is not None else self.__getitem__(node_name)
        sibling = self.__getitem__(sibling_name)
        if node.get('parent') == sibling.get('parent'):
            return True
        return False

    def has_siblings(self, node_name, sibling_names=[]):
        if len(sibling_names) == 0:
            return False
        num_siblings = 0
        node = self.__getitem__(node_name)
        for sibling_name in sibling_names:
            if self.has_sibling(
                    node_name, sibling_name=sibling_name, cached=node):
                num_siblings += 1
        return num_siblings == len(sibling_names)

    def is_match(self, node, node_name):
        return self.__getitem__(node_name).val == node_name

    def num_siblings(self, node_name):
        return len(self.get_siblings(node_name))

    def children_count(self, node_name):
        return len(self.__getitem__(node_name).get('edges', []))

    def prev_child(self, node_name, child_name):
        """Gets the previous child (adjacent) to this one. The returned node
        is the one that comes before `node_name`."""
        node = self.__getitem__(node_name)
        children = node.get('edges')
        num_children = len(children)
        try:
            child_index = children.index(child_name)
        except ValueError:
            return None
        # If this is the last, or the only one, raise an error.
        if child_index == num_children or num_children == 1:
            return None
        return self.__getitem__(children[child_index - 1])

    def next_child(self, node_name, child_name):
        """Gets the next child (adjacent) to this one. The returned node
        is the one that comes after `node_name`."""
        node = self.__getitem__(node_name)
        children = node.get('edges')
        num_children = len(children)
        try:
            child_index = children.index(child_name)
        except ValueError:
            return None
        # If this is the last, or the only one, raise an error.
        if child_index == num_children or num_children == 1:
            return None
        return self.__getitem__(children[child_index + 1])

    def add_sibling(self, key, node_name, data=None):
        """Add a node on the same level as this node."""
        new_node = Tree(node_name, data=data)
        # Make this sibling have the same parent.
        new_node.parent = self.parent
        # Update parent's children as well.
        self.parent['edges'].append(new_node)
        return new_node

    def add_child(self, node_name, new_key=None, new_vertices=[]):
        """Add a node below this node."""
        node = self.__getitem__(node_name)
        new_node = self.__setitem__(new_key, new_vertices, parent=node)
        node['edges'].append(new_node.name)
        return node

    def change_parent(self, node_name, parent_name=None):
        """Swap this nodes' parent with a new parent node."""
        node = self.__getitem__(node_name)
        new_parent = self.__getitem__(parent_name)
        old_parent = self.__getitem__(node.get('parent'))
        # Update this nodes parent
        node.update({'parent': parent_name})
        # Remove child from old parent
        old_parent.get('edges').remove(node_name)
        # Add child to new parent edges.
        new_parent.get('edges').append(new_parent)
        return node


class Forest(Tree):
    """Forest: A forest is a set of n ≥ 0 disjoint trees."""
    pass


if DEBUG:
    with Section('Tree ADT - the most basic form of a tree data structure.'):
        """
                            0  root
                           / \
                          /   \
                         1     2  interior
                        / \     \
                       /   \     \
                      3     4     5  interior
                     / \         / \
                    /   \       /   \
                   6     7     8     9  leaf
                  /
                 10  interior
                /  \
               /    \
              11    12  leaf

          The tree above is represented in python code below.

        """
        # `get` and `add_*` implement a chainable interface to allow for
        # fluid calls, which is particularly intuitive since every call puts
        # us at the specific node in question, like traversing the tree.

        graph = {
            0: {'edges': [1, 2], 'val': 'i am the root!', 'is_root': True},
            1: {'edges': [3, 4], 'val': '', 'parent': 0},
            2: {'edges': [5], 'val': 'i am greater than 1!', 'parent': 0},
            3: {'edges': [6, 7], 'val': '', 'parent': 1},
            4: {'edges': [], 'val': '', 'parent': 1},
            5: {'edges': [8, 9], 'val': '', 'parent': 2},
            6: {'edges': [], 'val': '', 'parent': 3},
            7: {'edges': [], 'val': 'lucky number 7', 'parent': 3},
            8: {'edges': [], 'val': '', 'parent': 5},
            9: {'edges': [], 'val': '', 'parent': 5},
            10: {'edges': [11, 12], 'val': '', 'parent': 6},
            11: {'edges': [], 'val': '', 'parent': 10},
            12: {'edges': [], 'val': '', 'parent': 10},
        }

        tree = Tree(graph)
        tree[9] = {'edges': [], 'val': '', 'parent': 5}
        prnt('Tree, subclassed from graph', tree)
        divider(newline=False)

        for n in range(len(graph)):
            print('Testing get: {} ... {}'.format(n, graph[n]))

        cmd_title('Testing: children_count', newlines=False)
        assert tree.children_count(1) == 2
        assert tree.children_count(2) == 1
        assert tree.children_count(3) == 2
        assert tree.children_count(9) == 0

        # Correctness testing

        cmd_title('Testing: get_root', newlines=False)
        assert tree.get_root().get('val') == 'i am the root!'
        tree[0].update({'val': 'i am still the root!'})
        assert tree.get_root().get('val') == 'i am still the root!'

        cmd_title('Testing: has_sibling', newlines=False)
        assert not tree.has_sibling(7, sibling_name=9)
        assert tree.has_sibling(8, sibling_name=9)

        cmd_title('Testing: node_height', newlines=False)
        assert tree.node_height(4) == 1
        assert tree.node_height(3) == 2
        assert tree.node_height(1) == 3
        assert tree.node_height(0) == 4

        cmd_title('Testing: node_depth', newlines=False)
        assert tree.node_depth(4) == 3
        assert tree.node_depth(3) == 3
        assert tree.node_depth(1) == 2
        assert tree.node_depth(0) == 1

        cmd_title('Testing: has_siblings', newlines=False)
        assert tree.has_siblings(6, sibling_names=[7])
        assert tree.has_siblings(8, sibling_names=[9])
        assert not tree.has_siblings(5, sibling_names=[4])
        assert tree.has_siblings(3, sibling_names=[4])

        cmd_title('Testing: total_height', newlines=False)
        assert tree.total_height() == 4

        cmd_title('Testing: is_descendant', newlines=False)
        assert tree.is_descendant(9, 2)
        assert tree.is_descendant(6, 3)
        assert not tree.is_descendant(6, 8)
        assert not tree.is_descendant(4, 7)

        cmd_title('Testing: is_ancestor', newlines=False)
        assert tree.is_ancestor(2, 9)
        assert tree.is_ancestor(1, 3)
        assert not tree.is_ancestor(4, 3)
        assert not tree.is_ancestor(8, 9)
        assert not tree.is_ancestor(6, 9)
        assert not tree.is_ancestor(3, 4)

        cmd_title('Testing: degree', newlines=False)
        assert tree.degree(1) == 2
        assert tree.degree(0) == 2
        assert tree.degree(4) == 0

        cmd_title('Testing: prev_child', newlines=False)
        assert tree.next_child(4, 1) is None
        assert tree.next_child(3, 6).get('val') == 'lucky number 7'
        assert tree.next_child(0, 1).get('val') == 'i am greater than 1!'

        cmd_title('Testing: next_child', newlines=False)
        assert tree.next_child(4, 1) is None
        assert tree.next_child(3, 6).get('val') == 'lucky number 7'
        assert tree.next_child(0, 1).get('val') == 'i am greater than 1!'

        cmd_title('Testing: is_leaf', newlines=False)
        assert tree[4].get('is_leaf')
        assert tree[6].get('is_leaf')
        assert tree[7].get('is_leaf')
        assert tree[8].get('is_leaf')
        assert tree[9].get('is_leaf')

        cmd_title('Testing: get_siblings', newlines=False)
        assert tree.get_siblings(4) == [3, 4]
        assert tree.get_siblings(6) == [6, 7]
        assert tree.get_siblings(8) == [8, 9]

        cmd_title('Testing: num_siblings', newlines=False)
        assert tree.num_siblings(4) == 2
        assert tree.num_siblings(6) == 2
        assert tree.num_siblings(8) == 2

        cmd_title('Testing: change_parent', newlines=False)
        tree.change_parent(4, parent_name=2)
        assert tree[4].get('parent') == 2

        assert len(graph) == 13
        del tree[4]
        assert len(graph) == 12
        del tree[10]
        assert len(graph) == 9
        assert tree.node_count == 10  # Inclusive

        assert tree.walk(4, 5) == []
        print(tree.walk(0, 4))
        assert tree.walk(0, 12) == []
