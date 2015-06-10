# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import cmd_title
from helpers.display import print_simple
from random import choice
from random import shuffle
import time


class DummyProgramGenerator:
    """A helper to generate programs for use in the Turing Machine
    -- useful for testing a Universal Turing Machine."""

    @staticmethod
    def _transition(next, symbols=[0, 1]):
        """Create a single transition pair with a random 0, 1
        write symbol (or provided symbol set."""
        return {'next': next, 'value': choice(symbols)}

    @staticmethod
    def make(max_states=10):
        """Make a program to run in the machine.

        Transitions are made up of key/value pairs,
        so it's important to shuffle the value beforehand.
        """
        states = range(max_states)
        keys = range(max_states)
        shuffle(keys)
        return {
            'states': states,
            'transitions': {
                keys[index]: DummyProgramGenerator._transition(state)
                for index, state in enumerate(states)}}


class TuringMachine(object):

    def __init__(self, program=None, max_states=10):
        self.DEBUG = False
        self.DELAY = 0.3
        self.result = ''
        self.transitions = {}
        self.max_states = max_states
        self.running = True
        self._setup(program)

    def _show_program(self):
        cmd_title('PROGRAM')
        print_simple('States list', self.states)
        print_simple('Transitions', self.transitions)
        print_simple('Tape', self.tape)

    def _setup(self, program):
        if program is None:
            self.program = DummyProgramGenerator.make(
                max_states=self.max_states)
        else:
            self.program = program
        self.states = self.program['states']
        # 'Blank' tape of zeros (technically infinite, but for now, finite)
        self.tape = [0 for _ in range(self.max_states * 2)]
        # Start the index in the 'middle' of the tape, a reasonable place.
        self.tape_index = len(self.tape) / 2
        # Associate states with the random group of keys previously generated
        self.transitions = self.program['transitions']
        # Randomize the current state
        self.current_state = self.transitions[choice(self.states)]

    def _get_tape_visualization(self):
        tape_viz = ' '.join(['[{}]'.format(value) for value in self.tape])
        idx = self.tape_index + 1 if self.tape_index == 0 else self.tape_index
        # 5 = 2 spaces, 2 brackets and number
        head_dist = idx * 5
        # length, no left/right space, (-2),
        # with 4 spaces per cell (3 chars + space)
        full_dist = (len(self.tape) * 4) - 2
        direction = self.current_state['next']
        track = '.'
        track_active = '_'
        left = track_active if direction == 0 else track
        right = track if direction == 0 else track_active
        # Print the "head" pointer
        pointer = (left * head_dist) + '^' + (right * (full_dist - head_dist))
        self.result += str(self.current_state['value'])
        print('{} == {}\n{}\n'.format(tape_viz, self.result, pointer))

    def _run(self):
        cmd_title('STARTING VISUALIZATION')
        while self.running:
            for _ in range(self.max_states):
                # Sleep so that each step is delayed, for effect.
                time.sleep(self.DELAY)
                if self.DEBUG:
                    print('Old state {}'.format(self.current_state))
                self.transition()
                if self.DEBUG:
                    print('New state {}'.format(self.current_state))
                    self._show_program()
                self._get_tape_visualization()
            if self.DEBUG:
                print('Ending with state: {}'.format(self.current_state))
            # Eventually time out, since it can't *really* run forever.
            self.halt()

    def run(self):
        if self.DEBUG:
            print(
                'Starting with current state:', self.current_state,
                'and tape index:', self.tape_index)
            self._show_program()
        self._run()

    def transition(self):
        # Update the new state 'pointer'
        new_state = self.transitions[self.current_state['next']]
        self.current_state = new_state
        # Update the tape index
        self.tape_index = new_state['next']
        # Write the new value to the head
        self.tape[self.tape_index] = new_state['value']

    def activate(self):
        cmd_title('ACTIVATING')
        self.running = True

    def halt(self):
        """Whether or not this machine actually does halt,
        this method must be called to prevent stack overflow
        (for infinite examples)."""
        cmd_title('HALTING')
        self.running = False
        # Reset any state
        self.tape = None
        self.transitions = None
        self.current_state = None
        self.tape_index = None
        self.result = ''


class Decider(TuringMachine):
    """See wikipedia.org/wiki/Machine_that_always_halts"""

    def transition(self):
        super(Decider, self).transition()
        # Stop aka "decide".
        self.halt()
        # Re-active for next time.
        self.activate()


if __name__ == '__main__':
    with Section('Turing Machines'):
        tm = TuringMachine()
        tm.run()
