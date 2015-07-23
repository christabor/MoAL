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

DEBUG = True if __name__ == '__main__' else False


class HypgerGraph(Graph):
    """
    From mathworld.wolfram.com/Hypergraph.html:
    "A hypergraph is a graph in which generalized edges (called hyperedges)
    may connect more than two nodes."

    Also interesting, from en.wikipedia.org/wiki/Hypergraph
    "The collection of hypergraphs is a category with hypergraph
    homomorphisms as morphisms."
    """


if DEBUG:
    with Section('Multi-graph'):
        hypergraph = HypgerGraph(dmkr.random_graph(max_edges=10))
        print_h3('Random multi-graph')
        print(hypergraph)
        # Multiple edges pointing to each other
        hypergraph2 = HypgerGraph({
            0: {'edges': [1, 2, 3], 'val': 'A'},
            1: {'edges': [0, 3, 2, 1], 'val': 'B'},
            2: {'edges': [0, 1, 3, 2], 'val': 'C'},
            3: {'edges': [0, 1, 2, 3], 'val': 'D'},
        })
        print(hypergraph2)
        if raw_input('Save graph images? Y/N: ') == 'Y':
            hypergraph.render_graph('hypergraph-test.png')
            hypergraph2.render_graph('hypergraph2-test.png')
