# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class Cell:

    programmed_cell_death = True

    def mitosis(self):
        raise NotImplementedError

    def mutate(self):
        raise NotImplementedError

    def copy_dna(self):
        raise NotImplementedError


class CancerCell(Cell):
    """Duck Typing, with a twist - it looks like a cell, moves like a cell...
    but it has a little surprise!"""

    programmed_cell_death = False


class Skin:

    tissue_type = 'skin'


class Teratoma(Skin):

    tissue_type = 'eyeball + teeth'


class VitalOrgan:
    """Fun side note - when an organ or part of the body is forming,
    it uses cell apoptosis to effectively 'carve out' the shape by killing
    off cells in a programmatic process -- amazing!

    See: https://en.wikipedia.org/wiki/Programmed_cell_death
    """

    def __init__(self, cells=[]):
        self.cells = cells
        self.differentiation_pattern = {}  # This would contain data

    def replenish(self, cells):
        self.cells += cells

    def differentiate(self):
        """Not to be confused with cell differentiation."""
        print('Differentiating!')


class ApoptosisManager:

    def autophagy(self, tissue):
        print('Autophagy: cleaning up old cells!')
        for cell in tissue.cells:
            if cell.programmed_cell_death:
                print('Killing off cell!')
            else:
                print('I AM A CANCER CELL - I WILL NOT DIE')


if DEBUG:
    with Section('SOME MODULE TITLE'):
        # Okay, so here's the rundown;
        # 1. New cells are created out of thin air, for something.
        # 2. They are associated with a vital organ -- that is to say,
        # they ARE the vital organ -- they make up the parts of it.
        # 3. An autophagy manager comes along as a process, to deal with cleanup
        # and delegation (a bit of a creative interpretation here).
        # 4. Manager attempts to clean up at the request of the organ,
        # only to find there is a hidden cancer cell hiding underneath.
        apoptos = ApoptosisManager()
        organ = VitalOrgan(cells=[Cell() for _ in range(5)] + [CancerCell()])
        apoptos.autophagy(organ)

        some_skin = Skin()
        some_other_skin = Teratoma()
        print(some_skin.tissue_type)
        # Oh god, wtf!
        print(some_other_skin.tissue_type)
