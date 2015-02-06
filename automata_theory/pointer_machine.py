# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import Section
from generic_helpers import _cmd_title
from fundamentals.graphs import Graph
from fundamentals.graphs import DirectedGraph
import time

# Definition, variations and example instruction set
# http://en.wikipedia.org/wiki/Pointer_machine


class PointerMachine(object):

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return type(self).__name__

    def __init__(self, program=None):
        self.DEBUG = False
        # Time delay, only used for only demonstration effect.
        self.DELAY = 0
        self._step = 0
        self.halted = False

    def halt(self):
        if self.DEBUG:
            _cmd_title('Halting')
        self.halted = True

    def run_instruction(self, instruction):
        if self.DEBUG:
            print 'Step ... #{} with instruction {} in register {}'.format(
                self._step, instruction['code'], self.curr_register)
            time.sleep(self.DELAY)
        # Prevent running if halted.
        if self.halted:
            return
        self._step += 1

    def run(self):
        while not self.halted:
            # For testing generated programs halting errors
            if self._step == 200:
                self.halt()
            self._step += 1
            self.run_instruction(self.program[self.curr_instruction])


# Wikipedia:
# "At least three major varieties exist in the literature:
# the Kolmogorov-Uspenskii model (KUM, KU-machine),
# the Knuth linking automaton,
# and the Schönhage Storage Modification Machine model (SMM).
# The SMM seems to be the most common."
# Also, http://en.wikipedia.org/wiki/
#   Pointer_machine#Types_of_.22Pointer_Machines.22

class KolmogorovUspenskii(PointerMachine):
    pass


class KnuthLinking(PointerMachine):
    pass


class SchonhageStorageModification(PointerMachine):

    def __init__(self, *args, **kwargs):
        super(SchonhageStorageModification, self).__init__(*args, **kwargs)
        self.state_graph = Graph()
        print 'GRAPH states'
        print self.state_graph
        self.state_graph[1] = [1, 3, 4, 10]
        self.state_graph[0] = [1, 2, 3]
        print self.state_graph.nodes
        print self.state_graph.view()


class AtomisticPureLISP(PointerMachine):
    pass


class AtomisticFullLISP(PointerMachine):
    pass


class GeneralAtomistic(PointerMachine):
    pass


class JonesIOne(PointerMachine):
    pass


class JonesITwo(PointerMachine):
    pass


with Section('Pointer Machines'):
    classes = [
        KolmogorovUspenskii, KnuthLinking, SchonhageStorageModification,
        AtomisticPureLISP, AtomisticFullLISP, GeneralAtomistic,
        JonesIOne, JonesITwo,
    ]

    for klass in classes:
        print
        print 'Testing machine...', repr(klass)
        klass().run()
