# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_success
from helpers.display import print_info
from random import randrange as rr


DEBUG = True if __name__ == '__main__' else False


class MemoryManager:

    def __init__(self):
        self.memory_blocks = {}
        self.last_block = 1
        self.MAX_RAM = 16000000000
        self.free_ram = self.MAX_RAM

    def __str__(self):
        print_success('Viewing applications in memory...')
        for node, ram_usage in self.memory_blocks.iteritems():
            print('--- {} | {} bytes @ {}'.format(
                node, sum([f[0] for f in ram_usage]),
                [f[1] for f in ram_usage]))
        return ''

    def _divvy_ram(self, ram):
        """This is an arbitrary, somewhat meaningless method, to simulate
        the notion of free blocks of ram that must be allocated and
        referenced via pointer. A given program may require X ram, but
        the location of available ram may be disparate, so various blocks have
        to be stored as a free linked list, or similar data structure.
        Since we've already covered linked lists, association lists, etc...,
        there isn't much value outside learning the context of this data
        structure, which tends to be in memory management."""
        subdivisions = rr(2, 20)  # Arbitrary number
        flist = []
        while subdivisions > 0:
            diff = rr(0, ram)
            # Store ram as [current block of memory, location]
            flist.append([diff, str(self.last_block).zfill(4)])
            ram = ram - diff
            self.last_block += 1
            subdivisions -= 1
            if DEBUG:
                print_info('Ram: {} / diff: {}'.format(ram, diff))
        return flist

    def malloc(self, item, ram):
        self.memory_blocks[item] = self._divvy_ram(ram)
        self.free_ram -= ram
        print('Ram decreased: {} ({} bytes)'.format(self.free_ram, ram))

    def free(self, item):
        ram = sum([f[0] for f in self.memory_blocks[item]])
        self.free_ram += ram
        print('Ram increased: {} ({} bytes)'.format(self.free_ram, ram))
        del self.memory_blocks[item]


if DEBUG:
    with Section('Free list - Memory Manager'):
        manager = MemoryManager()
        manager.malloc('itunes', 128000000)
        manager.malloc('photoshop', 256000000)
        manager.malloc('chrome', 64000000)
        print(manager)
        manager.free('photoshop')
        manager.free('itunes')
        print(manager)
