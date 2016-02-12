# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import prnt
from random import randrange
from copy import deepcopy
from random import choice
import pygraphviz as pgv

# Terminology from wikipedia.org/wiki/Glossary_of_graph_theory
# and base algorithm from cs.hmc.edu/~keller/courses/cs60/s98/examples/acyclic

MAX_VERTICES = 6
MAX_EDGES = MAX_VERTICES / 2
all_vertices = range(0, MAX_VERTICES)

DEBUG = True if __name__ == '__main__' else False


class InvalidGraphRepresentation(Exception):
    pass


class GraphRendererMixin:

    def build_graph(self, **kwargs):
        g = pgv.AGraph(**kwargs)
        for name, data in self.vertices.iteritems():
            g.add_node(name, label=data['val'] if data['val'] else name)
            for edge in data['edges']:
                g.add_edge(str(edge), str(name))
        return g

    def render_graph(self, filename, **kwargs):
        g = self.build_graph(**kwargs)
        g.layout()
        g.draw(filename)


class Graph(object, GraphRendererMixin):

    def __len__(self):
        _len = []
        for key in self.vertices:
            _len += self.vertices[key]['edges']
        return len(set(_len))

    def __init__(self, vertices={}):
        if not isinstance(vertices, dict):
            raise ValueError
        self.vertices = vertices
        self.node_count = 0

    def __contains__(self, vertex):
        try:
            vals = [f['val'] for f in self.vertices.values()]
        except KeyError:
            vals = []
        return vertex in self.vertices or vertex in vals

    def __setitem__(self, *args):
        key, vertices = args
        # Ensure it has no duplicate edges
        vertices['edges'] = list(set(vertices['edges']))
        vertices['node'] = key
        self.vertices[key] = vertices
        self.node_count += 1
        return self.vertices[key]

    def __delitem__(self, vertex):
        # Remove entire node
        if vertex not in self:
            return
        del self.vertices[vertex]
        # Remove other references.
        for vert in self.vertices:
            if vertex in self.vertices[vert]['edges']:
                self.vertices[vert]['edges'].remove(vertex)
        self.node_count -= 1

    def __getitem__(self, vertex):
        if vertex not in self.vertices:
            return None
        return self.vertices[vertex]

    def __iter__(self):
        return iter(self.vertices)

    def __reversed__(self):
        return reversed(self.iter())

    def __unicode__(self):
        return unicode(self.__repr__())

    def __repr__(self):
        return '{}'.format(self.vertices)

    def __str__(self):
        display = []
        for vertex, vertices in self.vertices.iteritems():
            display.append('({vertex}) --> {outbound}'.format(
                vertex=vertex, outbound=vertices['edges']))
        return ',\n'.join(display)

    def _add_inbound_edges(self):
        for k, v in self.vertices.iteritems():
            self._add_inbound_edge(k)

    def _add_inbound_edge(self, key):
        verts = self.vertices[key]
        if key not in verts['edges']:
            verts['edges'].append(key)

    def all_vertices(self, unique=True):
        """Return all vertices in the graph, including duplicate
        references; remove duplicates if `unique` is true."""
        vertices = self.vertices.keys()
        for vals in self.vertices.values():
            vertices = vertices + vals['edges']
        return list(set(vertices)) if unique else vertices

    def _has_vertex(self, vertex, verts):
        return vertex in verts

    def has_vertex(self, vertex, target):
        return target in self[vertex]['edges']

    def degree(self, vertex):
        """Return the number of edges for a given vertex.
        Only allows string/integer/tuple vertices."""
        try:
            return len(self.vertices[vertex]['edges'])
        except KeyError:
            return 0

    def has_degree(self, vertex, degrees):
        return self.degree(vertex) == degrees

    def has_multiple_degrees(self, vertex):
        return self.degree(vertex) > 1

    def is_open(self, start, end):
        return not self.is_closed(start, end)

    def is_closed(self, start, end):
        """A walk is considered closed if the first and last
        vertices are the same, open if not. This is also known as a cycle."""
        if start == end:
            return True
        res = self.walk(start, end, test_cycle=True)
        if len(res) == 0:
            return True
        return res[0] == res[-1]

    def _dfs(self, start, target):
        """Typical stack based DFS algorithm, translated from
        pseudocode via wikipedia.org/wiki/Depth-first_search"""
        stack = []
        seen = []
        stack.append(start)
        while len(stack) > 0:
            vertex = stack.pop()
            if vertex == target:
                return self[vertex]
            if vertex not in seen:
                seen.append(vertex)
                stack += self[vertex]['edges']
        if DEBUG:
            print(seen)
        return []

    def _bfs(self, start):
        raise NotImplementedError

    def is_leaf(self, vertex):
        """In a plain graph, a leaf vertex is a
        vertex with no outbound edges."""
        return self.degree(vertex) == 0

    def walk(self, start, end, path=[], test_cycle=False):
        path = path + [start]
        paths = []
        if test_cycle:
            end = start
        if start == end and not test_cycle:
            return path
        if test_cycle and path[-1] == start:
            return paths
        if start in self.vertices.keys():
            for vertex in self.vertices[start]['edges']:
                # Add new vertex if it's not in the list already.
                if vertex not in path:
                    # Get new path from this vertex
                    paths += self.walk(
                        vertex, end, path=path, test_cycle=test_cycle)
        return paths

    def _prune_all(self):
        """The pruning function of `is_acyclic`. Continue deleting
        vertices and checking if a cycle exists on any current vertex."""
        while len(self.vertices.keys()) > 1:
            verts = self.vertices.keys()
            # Get a new random vertex - yes, random is sufficient here.
            start = choice(verts)
            if DEBUG:
                print('Checking cycle... start={}, vertices={}'.format(
                    start, verts))
            # Skip ahead if there's only one vertex left.
            if self.is_cycle(start):
                return False
            else:
                # Otherwise, keep checking cycles and deleting vertices.
                self.__delitem__(start)

    def is_trail(self, start, end):
        """A trail is a walk in which all the edges are distinct."""
        res = self.walk(start, end)
        return len(res) == len(set(res))

    def is_bipartite(self, start, end):
        pass

    def tour_hamiltonian(self):
        pass

    def tour_eulerian(self):
        pass


class UndirectedGraph(Graph):

    def __init__(self, *args, **kwargs):
        super(UndirectedGraph, self).__init__(*args, **kwargs)
        self._add_inbound_edges()

    def __setitem__(self, *args):
        key, _ = args
        super(UndirectedGraph, self).__setitem__(*args)
        self._add_inbound_edge(key)


class DirectedGraph(Graph):

    def is_cycle(self, vertex):
        return self.walk(vertex, None, test_cycle=True)[::-1] == vertex

    def is_acycle(self, vertex):
        return not self.is_cycle(vertex)

    def is_cyclic(self):
        return not self.is_acyclic()

    def _is_acyclic(self):
        """A small method for the acyclic check that can be overridden,
        primarily for filtering behavior to override the return value
        of `is_acyclic`, depending on the inheriting data structure."""
        last_key = self.vertices.keys()[0]  # Only one vertex left.
        vertices_left = len(self.vertices[last_key]['edges'])
        is_acyclic = True if vertices_left == 0 else False
        if DEBUG:
            print('Graph {} acyclicity = {}'.format(self.vertices, is_acyclic))
        return is_acyclic

    def is_acyclic(self, restore=True):
        """A graph is acyclic if:
        * It has no vertices to begin with.
            [OR]
        * If continual removal of leaf vertices and
            updating of arcs leaves no vertices.
        If there is a non-leaf node left, the graph IS cyclic.
        """
        # A graph with no vertices is automatically acyclic.
        if len(self.vertices) == 0:
            return True
        # A graph with NO leaf vertices is cyclic.
        leaves = len([self.is_leaf(vertex) for vertex in self.vertices])
        if leaves == 0:
            return False
        # Keep a backup of the original graph.
        if restore:
            graph_copy = deepcopy(self.vertices)
        self._prune_all()
        # If a cycle wasn't found while pruning, it's guaranteed to be acyclic.
        is_acyclic = self._is_acyclic()
        # Restore backup
        if restore:
            self.vertices = graph_copy
        return is_acyclic

    def _dfs(self, start, target):
        """Same as above, but we consider outgoing and ingoing connections.
        Any node with no outgoing connections automatically stops traversal."""
        stack = []
        seen = []
        stack.append(start)
        while len(stack) > 0:
            vertex = stack.pop()
            outgoing = self[vertex]['edges']
            # If no outgoing edges exist, stop.
            if len(outgoing) == 0:
                return stack
            if vertex == target:
                return self[vertex]
            if vertex not in seen:
                seen.append(vertex)
                stack += self[vertex]['edges']
        if DEBUG:
            print(seen)
        return []


class CyclicGraph(Graph):
    pass


class DirectedCyclicGraph(DirectedGraph, CyclicGraph):
    pass


class DirectedAcyclicGraph(DirectedGraph):
    pass


def _rand_edges(num_edges):
    global all_vertices

    def _graph(num_edges):
        return [choice(all_vertices) for _ in range(num_edges)]
    edges = set(_graph(num_edges))

    # Since it's random, force unique graph
    while len(edges) < num_edges:
        edges = set(_graph(num_edges))
    return list(edges)


if DEBUG:
    with Section('Graph'):
        """Graphs are generated using a dictionary with labels.
        'edges' is a list of edges, and 'val' is the name, and key.
        The graph is keyed by the node name, which can be any valid
        dictionary key format (e.g. string, number, list, etc...)
        Optional parameters can be added to the dictionary,
        but of course they are not referenced here."""
        graph = UndirectedGraph({
            0: {'edges': [1, 2], 'val': 'A'},
            1: {'edges': [2, 0], 'val': 'B'},
            2: {'edges': [0], 'val': 'C'},
        })
        assert len(graph.walk(0, 3)) == 0  # non-existent node
        assert len(graph.walk(2, 1)) == 3  # unreachable node
        assert graph.is_closed(1, 2)  # Cycle
        assert graph.is_closed(0, 0)  # Trivial cycle
        assert graph.is_closed(2, 1)  # Cycle

        graph[3] = {'edges': [], 'val': 'D'}
        graph.all_vertices()
        prnt('Generated graph', graph.vertices)
        deg, vertex = randrange(0, MAX_EDGES), choice(all_vertices)
        print('Has degree {} ... {}? {}'.format(
            deg, vertex, graph.has_degree(deg, vertex)))

        for vertex in graph:
            print('Vertex {} has degree {}'.format(
                vertex, graph.degree(vertex)))
        prnt('graph', graph)
        prnt('Has multiple degrees?', graph.has_multiple_degrees(1))

    with Section('Directed Graph'):
        digraph = DirectedGraph()
        digraph.DEBUG = True
        for n in range(MAX_VERTICES):
            digraph[n] = {'edges': _rand_edges(MAX_EDGES), 'val': n}
        prnt('Generated directed-graph', digraph.vertices)
        prnt('Digraph', digraph)
        prnt('Get item:', digraph[4])
        digraph[3] = {'edges': [3, 2, 5], 'val': ''}
        prnt('Set item:', digraph[3])
        del digraph[2]
        prnt('Del item:', digraph)

    with Section('Directed Cyclic / Acyclic Graph (DCG / DAG)'):
        dag = DirectedAcyclicGraph({
            1: {'edges': [2], 'val': 'A'},
            2: {'edges': [3, 4], 'val': 'B'},
            3: {'edges': [], 'val': 'C'},  # intentionally empty
            4: {'edges': [5, 6], 'val': 'D'},
            5: {'edges': [6], 'val': 'E'},
            6: {'edges': [3], 'val': 'F'}
        })
        dag.DEBUG = True
        degr_test = [(1, 1), (2, 2), (3, 0), (4, 2), (5, 1), (6, 1)]
        for degs in degr_test:
            assert dag.is_trail(*degs)
            assert dag.has_degree(*degs)
        assert dag.is_acyclic()
        dag[6] = {'edges': [3, 4], 'val': ''}  # Create cyclic graph
        dag[4] = {'edges': [5], 'val': ''}

        dcg = DirectedCyclicGraph({
            1: {'edges': [2, 3, 1]},
            2: {'edges': [1, 3, 2]},
            3: {'edges': [1, 2, 3]}
        })
        for k in dcg.vertices:
            assert len(dcg.vertices[k]['edges']) > 0
        assert not dcg.is_acyclic()
        assert dcg.is_cyclic()
        # Add another more complex example for testing.
        # see upload.wikimedia.org/wikipedia/commons/thumb/3/39
        #   /Directed_acyclic_graph_3.svg
        #   /356px-Directed_acyclic_graph_3.svg.png
        dcg_wikipedia = DirectedAcyclicGraph({
            2: {'edges': [], 'val': 'A'},
            3: {'edges': [8, 10], 'val': 'B'},
            5: {'edges': [11], 'val': 'C'},
            7: {'edges': [8, 11], 'val': 'D'},
            8: {'edges': [9], 'val': 'E'},
            9: {'edges': [], 'val': 'F'},
            10: {'edges': [], 'val': 'G'},
            11: {'edges': [2, 9, 10], 'val': 'H'},
        })
        assert dcg_wikipedia._dfs(8, 5) == []
        assert 'A' in dcg_wikipedia
        assert 'H' in dcg_wikipedia
        assert 'h' not in dcg_wikipedia
        assert 'Z' not in dcg_wikipedia
        dcg_wikipedia.DEBUG = True
        for k, vert in enumerate(dcg_wikipedia.vertices):
            assert not dcg_wikipedia.is_cycle(k)
            assert dcg_wikipedia.is_acycle(k)
        assert dcg_wikipedia.is_acyclic()
        draw = raw_input('Create png example of graph? Y/N ')
        if draw == 'Y':
            filename = raw_input('Please enter a filename (png): ')
            dcg_wikipedia.render_graph(filename)
