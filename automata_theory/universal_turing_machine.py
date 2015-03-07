# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from automata_theory.turing_machine import TuringMachine
from automata_theory.turing_machine import DummyProgramGenerator
from pprint import pprint as ppr


class UnknownProgram(Exception):
    pass


class UniversalTuringMachine(TuringMachine):
    """
    wikipedia.org/wiki/Universal_Turing_machine
        #Example_of_universal-machine_coding

    "
    TS = Tape symbol
    TM = Tape-motion
    MC = M-configuration (instruction, state)
    P = Print-op

    ====================================================================
    MC |   TS   | P | TM | Final MC
    --------------------------------------------------------------------
    q1   blank    P0  R    q2
    q2   blank    E   R    q3
    q3   blank    P1  R    q4
    q4   blank    E   R    q1

    ====================================================================
    MC code | TS code | P code | TM code | Final MC code | 5-tuple
    --------------------------------------------------------------------
    DA        D         DC       R         DAA             DADDCRDAA
    DAA       D         D        R         DAAA            DAADDRDAAA
    DAAA      D         DCC      R         DAAAA           DAAADDCCRDAAAA
    DAAAA     D         D        R         DA              DAAAADDRDA

    Finally, the codes for all four 5-tuples are strung together into a code
    started by ";" and separated by ";" i.e.:
    ;DADDCRDAA;DAADDRDAAA;DAAADDCCRDAAAA;DAAAADDRDA
    "

    ...for our experiment, we'll just encode one string directly, and skip the
    table mapping, since they both represent the same thing,
    albeit with different string values.
    """

    def __init__(self, *args, **kwargs):
        super(UniversalTuringMachine, self).__init__(*args, **kwargs)
        self.programs = {'main': self.program}
        del self.program

    def run(self, name):
        if name not in self.programs:
            raise UnknownProgram('Program {} doesn\'t exist!'.format(name))
        print('Running {}'.format(name))
        # Assign it to the "active" program, then run as usual.
        self.program = self.programs[name]
        # "un" halt the program, since it normally terminates permanently.
        self.activate()
        # Setup new state variables again
        self._setup(self.program)

        # Encode and decode work, but aren't really used -- they're irrelevant
        # for this example, but fun to show.
        self.encode()
        self.decode()

        # Call original run method to actually run the program
        super(UniversalTuringMachine, self).run()

    def add_program(self, *args):
        name, program = args
        if self.DEBUG:
            prnt('Adding program', program, func=ppr)
        self.programs[name] = program

    def encode(self):
        """Not really necessary, but to emulate the behavior we translate
        our generated program into a single long string of values that
        can be decoded."""
        print('Encoding active program')
        transitions = self.program['transitions']
        code = ['S{};V{};N{}'.format(
                k, v['value'], v['next']) for k, v in transitions.iteritems()]
        code = ':'.join(code)
        print('{} ==> {}'.format(self.program, code))
        self.code = code

    def decode(self):
        """Re-assemble the string sequence into a real data structure
        -- not part of the typical UTM behavior, but signifies the need to
        decode the values into something usable."""
        print('Decoding active program')
        code = {
            int(n.split(';')[0][1]): {
                'value': int(n.split(';')[1][1]),
                'next': int(n.split(';')[2][1])
            }
            for n in self.code.split(':')}
        print(code)


if __name__ == '__main__':
    with Section('Universal Turing Machine'):
        program = DummyProgramGenerator.make(max_states=5)
        prnt('UTM program', program, func=ppr)
        utm = UniversalTuringMachine(program=program)

        # Add some seed "programs"
        for n in range(4):
            utm.add_program(
                'program-{}'.format(n),
                DummyProgramGenerator.make(max_states=4))

        utm.run('program-0')
        utm.run('program-1')
