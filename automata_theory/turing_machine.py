# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import section
from generic_helpers import _cmd_title
from pprint import pprint as ppr
from random import choice
from random import shuffle
import time


class TuringMachine:

    def __init__(self, max_states=10):
        self.DEBUG = False
        self.DELAY = 0.5
        self.transitions = {}
        self.max_states = max_states
        self.running = True
        self.states_list = [_ for _ in range(self.max_states)]
        # 'Blank' tape of zeros (technically infinite, but for now, finite)
        self.tape = [0 for _ in range(20)]
        shuffle(self.states_list)
        # Start the index in the 'middle' of the tape, a reasonable place.
        self.tape_index = len(self.tape) / 2
        # Associate states with the random group of keys previously generated
        self._seed_states()
        # Randomize the current state
        self.current_state = self.transitions[choice(self.states_list)]
        _cmd_title('STARTING')
        self._get_tape_visualization()
        if self.DEBUG:
            print (
                'Starting with current state:', self.current_state,
                'and tape index:', self.tape_index)

    def _show_states(self):
        print 'States:', self.states_list

    def _get_tape_visualization(self):
        print ' '.join(['[{}]'.format(value) for value in self.tape])
        idx = self.tape_index + 1 if self.tape_index == 0 else self.tape_index
        # 5 = 2 spaces, 2 brackets and number
        head_dist = idx * 5
        # length, no left/right space, (-2),
        # with 4 spaces per cell (3 chars + space)
        full_dist = (len(self.tape) * 4) - 2
        _dir = self.current_state['next']
        track = '.'
        track_active = '_'
        left = track_active if _dir == 0 else track
        right = track if _dir == 0 else track_active
        # Print the "head" pointer
        print
        print (left * head_dist) + '^' + (right * (full_dist - head_dist))
        print

    def new_state(self, next):
        return {
            'next': next,
            'value': choice([0, 1])
        }

    def _seed_states(self):
        # Use previously shuffled array values from initial seeding
        self.transitions = {
            k: self.new_state(val) for val, k in enumerate(self.states_list)
        }
        if self.DEBUG:
            print
            print 'New states'
            ppr(self.transitions)
            print

    def run(self):
        while self.running:
            for _ in range(self.max_states):
                # Sleep so that each step is delayed, for effect.
                time.sleep(self.DELAY)
                if self.DEBUG:
                    print 'Old state', self.current_state
                self.transition()
                if self.DEBUG:
                    print 'New state', self.current_state
                    self._show_states()
                self._get_tape_visualization()
            if self.DEBUG:
                print 'Ending with state:', self.current_state
            # Eventually time out, since it can't really run forever.
            self.halt()

    def transition(self):
        # Update the new state 'pointer'
        new_state = self.transitions[self.current_state['next']]
        self.current_state = new_state
        # Update the tape index
        self.tape_index = new_state['next']
        # Write the new value to the head
        self.tape[self.tape_index] = new_state['value']

    def halt(self):
        """Whether or not this machine actually does halt,
        this method must be called to prevent stack overflow."""
        self.running = False
        _cmd_title('HALTING')


section('BEGIN - Probability')

tm = TuringMachine()
tm.run()

section('END - Probability')
