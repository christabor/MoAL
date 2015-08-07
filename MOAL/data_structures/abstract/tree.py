# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import prnt
from MOAL.helpers.display import divider
from MOAL.helpers.display import cmd_title
from MOAL.data_structures.graphs.graphs import Graph


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

    *Note*: the key used by graphs is simply edges, because direction or
    subordinate/dominant relationships are not relevant. Here, any edge from
    one node to another is implicitly downward, so specifying 'children' vs.
    'parent' is not necessary; all edges are considered children.
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
        # connections between the node and the root.
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

    def __setitem__(self, key, node):
        # Make sure they're unique.
        node['edges'] = set(node['edges'])
        # Prevent linking to oneself
        if key in node['edges']:
            node['edges'].remove(key)
        # Set root to False if not specified, otherwise True
        node.update({'is_root': node.get('is_root', False)})
        node.update({'is_child': not node.get('is_root', True)})
        node.update({'val': node.get('val', '')})
        node.update({'edges': node.get('edges', [])})
        is_leaf = len(node.get('edges')) == 0
        node.update({'is_leaf': is_leaf})
        node.update({'parent': node.get('parent', None)})
        super(Tree, self).__setitem__(key, node)
        return node

    def build_tree(self, **kwargs):
        g = super(Tree, self).build_graph(**kwargs)
        for name, data in self.vertices.iteritems():
            g.add_subgraph(data['edges'])
        return g

    def render_tree(self, filename, **kwargs):
        g = self.build_tree(**kwargs)
        g.layout(prog='dot')
        g.draw(filename)

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
        return self.__getitem__(node_name).get('val') == node_name

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

    def add_sibling(self, node_name, new_node_name, data={}):
        sibling = self.__getitem__(node_name)
        parent = sibling['parent']
        # Make this sibling have the same parent.
        data = {'val': data, 'parent': parent, 'edges': []}
        # # Update parent's children as well.
        self.vertices[parent]['edges'].append(node_name)
        self.__setitem__(new_node_name, data)
        return data

    def remove_child(self, node_name, child):
        """Add a node below this node."""
        node = self.__getitem__(node_name)
        node['edges'].remove(child)
        return node

    def add_child(self, parent, new_key, new_vertices=[]):
        """Add a node below this node."""
        parent_node = self.__getitem__(parent)
        new_node = {'parent': parent, 'edges': []}
        parent_node['edges'].append(new_key)
        self.__setitem__(new_key, new_node)
        return new_node

    def add_siblings(self, node_name, node_names):
        sibling = self.__getitem__(node_name)
        for new in node_names:
            # Update existing
            sibling['edges'].append(new)
            # Add new node
            self.__setitem__(new, {'edges': []})

    def change_parent(self, node_name, parent_name=None):
        """Swap this nodes' parent with a new parent node."""
        node = self.__getitem__(node_name)
        new_parent = self.__getitem__(parent_name)
        old_parent = self.__getitem__(node.get('parent'))
        # Update this nodes parent
        node.update({'parent': parent_name})
        # Remove child from old parent edges
        old_parent.get('edges').remove(node_name)
        # Add child to new parent edges
        new_parent.get('edges').append(node_name)
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

        graph = {
            0: {'edges': [1, 2], 'val': 'i am the root!', 'is_root': True},
            1: {'edges': [3, 4], 'parent': 0},
            2: {'edges': [5], 'val': 'i am greater than 1!', 'parent': 0},
            3: {'edges': [6, 7], 'parent': 1},
            4: {'edges': [], 'parent': 1},
            5: {'edges': [8, 9], 'parent': 2},
            6: {'edges': [10], 'parent': 3},
            7: {'edges': [], 'val': 'lucky number 7', 'parent': 3},
            8: {'edges': [], 'parent': 5},
            9: {'edges': [], 'parent': 5},
            10: {'edges': [11, 12], 'parent': 6},
            11: {'edges': [], 'parent': 10},
            12: {'edges': [], 'parent': 10},
        }

        tree = Tree(graph)
        tree[9] = {'edges': [], 'parent': 5}
        prnt('Tree, subclassed from graph', tree)
        tree.render_tree('tree-example.png')
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
        assert tree.node_height(3) == 4
        assert tree.node_height(1) == 5
        assert tree.node_height(0) == 6

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
        assert tree.total_height() == 6

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
        assert not tree[2].get('is_leaf')
        assert not tree[5].get('is_leaf')
        assert not tree[6].get('is_leaf')
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

        cmd_title('Testing: add_sibling', newlines=False)
        tree.add_sibling(9, 11)

        assert tree[11]['parent'] == tree[9]['parent']
        assert 11 not in tree[9]['edges']
        assert 9 not in tree[11]['edges']

        cmd_title('Testing: add_child', newlines=False)
        tree.add_child(9, 12)
        tree.add_child(9, 13)

        assert 12 in tree[9]['edges']
        assert 13 in tree[9]['edges']

        del tree[11]
        tree.add_siblings(9, [100, 101, 102])

        assert 100 in tree[9]['edges']
        assert 101 in tree[9]['edges']
        assert 102 in tree[9]['edges']

        """From Wikipedia:
        "An octree is a tree data structure in which each internal node
        has exactly eight children. Octrees are the three-dimensional
        analog of quadtrees. Octrees are often used in 3D graphics and
        3D game engines." - en.wikipedia.org/wiki/Octree
        """
        quadtree = Tree({
            1: {'edges': [2, 3, 4, 5], 'val': 'quadroot', 'is_root': True},
            2: {'edges': [], 'parent': 1},
            3: {'edges': [6, 7, 8, 9], 'parent': 1},
            4: {'edges': [], 'parent': 1},
            5: {'edges': [], 'parent': 1},
            6: {'edges': [], 'parent': 4},
            7: {'edges': [], 'parent': 4},
            8: {'edges': [], 'parent': 4},
            9: {'edges': [], 'parent': 4},
        })
        print(quadtree)
        quadtree.render_tree('quadtree-example.png')
        octree = Tree({
            0: {'edges': [1, 2, 3, 4, 5, 6, 7, 8], 'is_root': True},
            1: {'edges': [], 'parent': 0},
            2: {'edges': [], 'parent': 0},
            3: {'edges': [], 'parent': 0},
            4: {'edges': [9, 10, 11, 12, 13, 14, 15, 16], 'parent': 0},
            5: {'edges': [], 'parent': 0},
            6: {'edges': [], 'parent': 0},
            7: {'edges': [], 'parent': 0},
            8: {'edges': [], 'parent': 0},
            9: {'edges': [], 'parent': 4},
            10: {'edges': [], 'parent': 4},
            11: {'edges': [], 'parent': 4},
            12: {'edges': [], 'parent': 4},
            13: {'edges': [], 'parent': 4},
            14: {'edges': [], 'parent': 4},
            15: {'edges': [], 'parent': 4},
            16: {'edges': [], 'parent': 4},
        })
        print(octree)
        octree.render_tree('octree-example.png')
