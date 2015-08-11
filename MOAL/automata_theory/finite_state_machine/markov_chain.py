# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_info
from MOAL.data_structures.graphs.graphs import DirectedGraph
from pprint import pprint as ppr
from random import choice

DEBUG = True if __name__ == '__main__' else False


class InvalidProbabilityValue:
    pass


class MarkovChain(DirectedGraph):

    def __init__(self, *args, **kwargs):
        super(MarkovChain, self).__init__(*args, **kwargs)
        for node, data in self.vertices.iteritems():
            self._check_valid(node, data)
        # Keep a reference to all timestep values
        self.probabilities = []

    def __setitem__(self, node, data):
        self._check_valid(node, data)
        super(MarkovChain, self).__setitem__(node, data)

    def _check_valid(self, node, data):
        total = sum([prob for prob in data['edges'].values()])
        # Edges must sum to 1 (e.g 0.4, 0.5, 0.1)
        if total != 1:
            raise InvalidProbabilityValue

    def _update_proability(self, node, state):
        # Cut probability in half.
        self[node]['edges'][state] *= 0.5

    def _get_cell(self, node, state):
        return self[node]['edges'][state]

    def _get_all_probabilities(self):
        return [node['edges'] for label, node in self.vertices.iteritems()]

    def _step(self):
        # Keep track of previous set of probabilities
        self.probabilities.append(self._get_all_probabilities())
        # Runs through all nodes and updates their probabilities.
        # Typically it just cuts the value in half, but it can be updated
        # differently via `_update_probability`.
        for node, data in self.vertices.iteritems():
            for edge, prob in data['edges'].iteritems():
                old = self._get_cell(node, edge)
                self._update_proability(node, edge)
                new = self._get_cell(node, edge)
                print('Updated Cell: {} -> {}'.format(old, new))

    def step_n(self, count):
        for n in xrange(count):
            self._step()

    def view_probability_history(self):
        ppr(self.probabilities)

    def view_probability_history_of(self, node):
        probabilities = []
        for timestep in self.probabilities:
            for node_data in timestep:
                for node_label, value in node_data.iteritems():
                    if node_label == node:
                        probabilities.append(value)
        ppr({node: probabilities})

    def run(self, node, max=10):
        val = ''
        count, node = 0, self[node]
        print_info('[RUN]: node: {}'.format(node), prefix='[Running]')
        absorbing_states = False
        while count < max and not absorbing_states:
            # Once the node transitions from a probability edge,
            # the optional generator function allows any arbitrary data to be
            # generated. It can be deterministic or not
            # -- whatever the user wants to do.
            if 'generator' in node:
                val += '{}'.format(node['generator']())
            highest = 0
            # Update the active node based on which probability of the outgoing
            # edges for this node is the highest, then transition to that node.
            for edge, probability in node['edges'].iteritems():
                if probability == 1:
                    absorbing_states = True
                    break
                if probability > highest:
                    highest = probability
                    node = self[edge]
                self._step()
            print('{}Current node: {}, highest probability: {}'.format(
                count * ' ', edge, highest))
            count += 1
        print('Final value: {}'.format(val))
        return val

    def __iter__(self):
        for node, data in self.vertices.iteritems():
            yield node, data


def rand_flip():
    return choice([0, 1])


if DEBUG:
    with Section('Finite State Machine - Markov Chain'):
        example1 = MarkovChain({
            'E': {'edges': {'A': 0.7, 'E': 0.3}, 'val': 'E-node'},
            'A': {'edges': {'A': 0.6, 'E': 0.4}, 'val': 'A-node'}},)
        print(example1)

        try:
            test = MarkovChain({'E': {'edges': {'A': 1, 'E': 1}}})
        except InvalidProbabilityValue:
            print('Invalid test passed')

        example1.step_n(4)
        example1.view_probability_history()
        example1.view_probability_history_of('A')

        coinflip = MarkovChain({
            'S0': {'edges': {'S1': 0.5, 'S2': 0.5}, 'val': 'Flip'},
            # These are considered absorbing states
            'S1': {'edges': {'S0': 0.7, 'S2': 0.3}, 'val': 'Tails'},
            'S2': {'edges': {'S0': 0.3, 'S1': 0.7}, 'val': 'Heads'},
        })
        # Inject generator function automatically (because I'm lazy)
        for k, node in coinflip:
            node['generator'] = rand_flip

        coinflip.run('S0')
