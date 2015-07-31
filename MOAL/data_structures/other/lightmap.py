# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_simple
from random import randrange as rr

DEBUG = True if __name__ == '__main__' else False


class Lightmap:
    """
    From Wikipedia:
    "A lightmap is a data structure which contains the brightness of
    surfaces in 3d graphics applications such as video games.
    Lightmaps are pre-computed, and normally used for static objects only.
    They are particularly suited to urban and
    indoor environments with large planar surfaces."
    """

    def __init__(self, height=10, width=10):
        self.height = height
        self.width = width
        self.lighting = []

    def __str__(self):
        """This is a ...weird... method, but it's SOME way to
        visualize the notion of lighting, as darkness and lightness.
        Since I can't be bothered to actually build a real renderer for this
        project, I'm doing this to illustrate the idea in a fun(?) way.
        """
        fake_display = ''
        for k, pixel in enumerate(self.lighting):
            if pixel > 200:
                fake_display += '#'
            elif pixel > 100:
                fake_display += '@'
            elif pixel > 50:
                fake_display += '+'
            else:
                fake_display += '.'
            if k % self.width == 0:
                fake_display += '\n'
        print(fake_display)
        return ''

    def compute(self, recipe=1):
        """Don't be confused: the notion of a recipe is just for fun here.
        It has nothing to do with lightmaps -- it's just to experiment
        with example 'ascii lighting' for more interesting visualizations.
        """
        self.lighting = []
        pixels = self.height * self.width
        if recipe == 1:
            for k in xrange(pixels):
                self.lighting.append(rr(0, 255))
        elif recipe == 2:
            for k in xrange(pixels):
                self.lighting.append(rr(0, (k + 1) * 5))
        elif recipe == 3:
            for k in xrange(pixels):
                if self.width < self.height:
                    self.lighting.append(rr(self.width, self.height))
                else:
                    self.lighting.append(rr(self.height, self.width))


if DEBUG:
    with Section('Lightmap - 3d renderer'):
        lightmap = Lightmap(height=10, width=80)
        lightmap.compute()
        print_simple(lightmap, 'recipe #1')

        lightmap.compute(recipe=2)
        print_simple(lightmap, 'recipe #2')

        lightmap.compute(recipe=3)
        print_simple(lightmap, 'recipe #3')
