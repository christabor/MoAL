# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import print_success
from MOAL.helpers.display import print_error
from MOAL.helpers.display import print_info
from MOAL.helpers.display import divider

DEBUG = True if __name__ == '__main__' else False


class InvalidTransition:
    pass


class FiniteStateMachine(object):

    def __init__(self, states={}, default=None, debug=False, max=20):
        self.debug = debug
        # Used for stopping any non-halting auto-generated FSMs
        self.max = max
        self.states = states
        self.default = default
        self.current = self.default
        self.step = 0
        self.string = ''
        self.value = ''

    def __getitem__(self, state):
        return self.states[state]

    def __delitem__(self, state):
        del self.states[state]

    def __setitem__(self, state, data):
        self.states[state] = data

    def __str__(self):
        for node, data in self.states.iteritems():
            print('State {}'.format(node))
            if type(data) != dict:
                divider(newline=False)
                continue
            for state, transition in data['transitions'].iteritems():
                print('   {} --> ({})'.format(state, transition))
            divider(newline=False)
        return ''

    def reset(self):
        self.step = 0
        self.current = self.default

    def _xform(self, edge):
        """Allows customization of coercion function, for the transition
        key type, and/or index naming convention - some require ints,
        some strings, multiple nested indices, etc... This removes the
        requirement to override _get_transition with a lot more code."""
        return int(edge)

    def _get_transition(self, edge):
        try:
            return self.states[self.current]['transitions'][self._xform(edge)]
        except KeyError:
            raise InvalidTransition

    def _get_current(self):
        try:
            return self.current, self.states[self.current]
        except KeyError:
            return None, None

    def _print(self, edge, old, new):
        print('{} Transition: {} ({} -> {})'.format(
            self.step * ' ', edge, old, new))

    def transition(self, edge):
        old, old_data = self._get_current()
        self.current = self._get_transition(edge)
        new, new_data = self._get_current()
        self._print(edge, old, new)
        return new_data

    def get_next_value(self, node, edge):
        if node not in self.states:
            return None
        _node = self.states[node]['transitions']
        if _node is None or edge not in _node:
            return None
        return _node[edge]

    def _set_current(self, node_label):
        self.current = node_label


class Acceptor(FiniteStateMachine):

    def test(self, string):
        try:
            print_info('{}'.format(string), prefix='[TESTING]')
            chars = list(str(string))
            for char in chars:
                self.step += 1
                self.transition(char)
            self.reset()
            print_success(''.join(chars), prefix='[FOUND]')
            return True
        except InvalidTransition:
            print_error(''.join(chars), prefix='[NOT-FOUND]')
            return False


class Classifier(Acceptor):
    """From Wikipedia:
    "Classifier is a generalization that, similar to acceptor,
    produces single output when terminates but has more
    than two terminal states." """

    def classify(self, *args, **kwargs):
        return super(Classifier, self).test(*args, **kwargs)


if DEBUG:
    with Section('Finite State Machine'):
        # Example creation of
        # en.wikipedia.org/wiki/Finite-state_machine#/media/File:DFAexample.svg
        print_h2('FSM - Acceptor')
        acceptor = Acceptor(
            states={
                'S1': {'transitions': {0: 'S2', 1: 'S1'}, 'val': 'End node'},
                'S2': {'transitions': {0: 'S1', 1: 'S2'}, 'val': 'Start node'}},
            default='S1')
        assert acceptor.test('01100101011')
        assert acceptor.test('11')
        assert not acceptor.test('113')
        assert acceptor.test('1110001010')
        assert acceptor.test('0')
        assert acceptor.test('1')
