# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from helpers.display import Section
from helpers.display import _print
from helpers.display import _cmd_title
from pprint import pprint as ppr
from random import choice
import time


# Definition, variations and example instruction set
# from http://en.wikipedia.org/wiki/Counter_machine


class CounterMachine:

    def __str__(self):
        return type(self).__name__

    def __init__(self, program=None):
        """Setup initial conditions

        Function argument reference [From Wikipedia]
        ------------------------------------------------------------------
        Register #2 contains "2", (initially)
        Registers #0, #1 and #3 are empty (contain "0").
        Register #0 remains unchanged throughout calculations
            because it is used for the unconditional jump.
        Register #1 is a scratch pad.

        4 registers, plus 'scratch pad register'"

        `z` = [z]ero aka, jump register (0)
        `s` = [s]cratch register (1)
        `c` = [c]urrent register (2)
        `d` = [d]estination register (3)

        Example instruction set used for the initial program.
        ------------------------------------------------------------------
        1   2   3   4   5   6   7   8   9   10  <- Instruction (address)
        JZ  DEC INC INC JZ  JZ  DEC INC JZ  H   <- Instruction
        2   2   3   1   0   1   1   2   0       <- Register
        6               1   10          6       <- Jump-to instruction

        """
        self.DEBUG = True
        # Time delay, only used for only demonstration effect.
        self.DELAY = 0
        if self.DEBUG:
            _cmd_title('Prepping')
        if program is None:
            self.program = {
                1: {'code': 'JZ', 'fn': self.jz, 'reg': 2, 'jump': 6},
                2: {'code': 'DEC', 'fn': self.dec, 'reg': 2, 'jump': None},
                3: {'code': 'INC', 'fn': self.inc, 'reg': 3, 'jump': None},
                4: {'code': 'INC', 'fn': self.inc, 'reg': 1, 'jump': None},
                5: {'code': 'JZ', 'fn': self.jz, 'reg': 0, 'jump': 1},
                6: {'code': 'JZ', 'fn': self.jz, 'reg': 1, 'jump': 10},
                7: {'code': 'DEC', 'fn': self.dec, 'reg': 1, 'jump': None},
                8: {'code': 'INC', 'fn': self.inc, 'reg': 2, 'jump': 0},
                9: {'code': 'JZ', 'fn': self.jz, 'reg': 0, 'jump': 6},
                10: {'code': 'H', 'fn': self.halt, 'reg': None, 'jump': None},
            }
        else:
            self.program = program
        self.halted = False
        # Internal tracking of how many steps have been run - has no bearing
        # on the actual control flow or outcome of the program.
        self._step = 0
        self.default_register_count = 2
        self.curr_register = self.default_register_count
        # The program begins with instruction 1
        # (aka index 1 -- if the index is off, the program
        # will not run correctly, and may raise KeyErrors).
        self.curr_instruction = 1
        self.registers = {'z': 0, 's': 0, 'c': 2, 'd': 0, '': 0}

    def _generate_program(self, instructions=10, registers=4):
        # These programs are likely inoperable,
        # but are here just for fun/testing
        _registers = [_ for _ in range(registers)]
        _funcs = [
            'clr', 'inc', 'dec', 'cpy', 'jzdec', 'j', 'jz', 'je', 'jnz', ]
        _jump = [None, None] + _registers
        self.program = {}
        for instruction in range(instructions):
            fn = choice(_funcs)
            self.program[instruction] = {
                'code': fn.upper(),
                'fn': getattr(self, fn),
                'reg': choice(_registers),
                'jump': choice(_jump)
            }

    def halt(self):
        if self.DEBUG:
            _cmd_title('Halting')
        self.halted = True
        # From Wikipedia:
        # The program HALTs with the contents of register #2
        # at its original count and the contents of register #3
        # equal to the original contents of register #2...
        cnt = self.registers['c']
        # Update register three
        self.registers['d'] = cnt
        # Reset register 2 after transferring contents to register #3
        self.registers['c'] = self.default_register_count
        if self.DEBUG:
            print 'Final contents of all registers:', self.registers

    def run_instruction(self, instruction):
        if self.DEBUG:
            print 'Step ... #{} with instruction {} in register {}'.format(
                self._step, instruction['code'], self.curr_register)
            time.sleep(self.DELAY)
        # Prevent running if halted.
        if self.halted:
            return
        # After the instruction has been run, jump, if specified.
        if instruction['jump'] is not None:
            self.j(instruction['jump'])
        # Call the function
        instruction['fn']()
        # Update the register
        self.curr_register = instruction['reg']
        # Update global step counter
        self._step += 1

    def clr(self, c=2):
        self.registers['c'] = 0

    def inc(self, c=2):
        self.registers['c'] += 1

    def dec(self, c=2):
        self.registers['c'] -= 1

    def cpy(self, c=2, d=3):
        val = self.registers['c']
        self.registers['d'] = val

    def jzdec(self, c=2):
        if self.registers['c'] is None:
            self.j(c=c)
        else:
            self.registers['c'] -= 1

    def j(self, z=0):
        self.curr_instruction = z

    def jz(self, c=2, z=0):
        if self.registers['c'] == 0:
            self.j(z=z)

    def je(self, r_j, r_k, z=0):
        raise NotImplementedError

    def jnz(self, c=2, z=0):
        raise NotImplementedError

    def run(self):
        while not self.halted:
            # For testing generated programs halting errors
            if self._step == 100:
                self.halt()
            self.run_instruction(self.program[self.curr_instruction])


"""The way each machine is run is basically the same, but each
sub-classed machine may implement the primitive functions differently."""


class SheperdsonSturgis(CounterMachine):

    def jnz(self, c=2, z=0):
        if self.registers['c'] != 0:
            self.j()


class Minsky(CounterMachine):

    def inc(self, c=2, z=0):
        self.registers['c'] += 1
        self.j(z=z)

    def jzdec(self, c=2):
        raise NotImplementedError


class Program(CounterMachine):
    pass


class Abacus(CounterMachine):

    def inc(self, c=2, z=0):
        raise NotImplementedError


class Lambek(CounterMachine):
    pass


class Successor(CounterMachine):
    pass


class SuccessorRAM(CounterMachine):
    pass


class ElgotRobinsonRASP(CounterMachine):
    pass


if __name__ == '__main__':
    with Section('Counter Machines'):
        classes = [
            SheperdsonSturgis, Minsky, Program, Abacus, Lambek,
            Successor, SuccessorRAM, ElgotRobinsonRASP,
        ]

        for klass in classes:
            _print('Testing machine...', repr(klass))
            klass().run()

            _cmd_title('New program')
            singleton = CounterMachine()
            singleton._generate_program()
            ppr(singleton.program)
            try:
                singleton.run()
            except TypeError:
                print 'Inoperable program was generated :('
            finally:
                singleton.halt()
