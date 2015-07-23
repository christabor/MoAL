# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h3
from MOAL.helpers import datamaker as dmkr
from MOAL.data_structures.graphs.graphs import Graph
import pygraphviz as pgv

DEBUG = True if __name__ == '__main__' else False


class MultiGraph(Graph):

    def render_graph(self, filename, **kwargs):
        """Override the rendered, allowing color specification for
        loops vs. normal edges"""
        g = pgv.AGraph(**kwargs)
        for name, data in self.vertices.iteritems():
            g.add_node(name)
            curr = g.get_node(name)
            curr.attr['label'] = data['val'] if data['val'] else name
            for edge in data['edges']:
                if edge == name:
                    g.add_edge(str(edge), str(name), color='red')
                else:
                    g.add_edge(str(edge), str(name), color='blue')
        g.layout()
        g.draw(filename)


class LooplessMultiGraph(MultiGraph):
    """From Wikipedia:
        "Not all authors allow multigraphs to have loops."
    """

    def __init__(self, vertices={}):
        for vertex, data in vertices.iteritems():
            if vertex in data['edges']:
                raise ValueError(
                    'Loop "{}" is not allowed on vertices.'.format(vertex))
        return super(LooplessMultiGraph, self).__init__(vertices=vertices)

    def __setitem__(self, *args):
        key, vertices = args
        if key in vertices['edges']:
            raise ValueError('Loop {} is not allowed on vertices.'.format(key))
        return super(LooplessMultiGraph, self).__setitem__(*args)

if DEBUG:
    with Section('Multi-graph'):
        mgraph_rand = MultiGraph(dmkr.random_graph(max_edges=5))
        print_h3('Random multi-graph')
        print(mgraph_rand)
        # Multiple edges pointing to each other
        mgraph = MultiGraph({
            0: {'edges': [1, 2, 3], 'val': 'A'},
            1: {'edges': [0, 3, 2, 1], 'val': 'B'},
            2: {'edges': [0, 1, 3, 2], 'val': 'C'},
            3: {'edges': [0, 1, 2, 3], 'val': 'D'},
        })

        print_h3('Specific multi-graph')
        print(mgraph)
        mgraph.render_graph('mgraph.png', strict=False)

        print_h3('Specific loopless multi-graph')
        try:
            lmgraph = LooplessMultiGraph({
                0: {'edges': [1, 2, 3], 'val': 'A'},
                1: {'edges': [0, 3, 2, 1], 'val': 'B'},
                2: {'edges': [0, 1, 3, 2], 'val': 'C'},
                3: {'edges': [0, 1, 2, 3], 'val': 'D'},
            })
        except ValueError:
            lmgraph = LooplessMultiGraph({
                0: {'edges': [1, 2, 3], 'val': 'A'},
                1: {'edges': [0, 3, 2], 'val': 'B'},
                2: {'edges': [0, 1, 3], 'val': 'C'},
                3: {'edges': [0, 1, 2], 'val': 'D'},
            })
            print(lmgraph)
