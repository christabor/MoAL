# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
import mlpy
import matplotlib.pyplot as plot
import matplotlib.cm as cm
from random import randrange as rr

DEBUG = True if __name__ == '__main__' else False


def random_timesequence(start, end, steps=3):
    seq = []
    for n in range(start, end):
        # Randomize the number of sub-steps,
        # but maintain the bounds and monotonicity
        # (e.g. 0, 0, 1, 1, 1, 2, 3, 3, 3)
        for i in range(rr(0, steps)):
            seq.append(n)
    return seq


if DEBUG:
    with Section('Dynamic Time Warping algorithm - MLPY'):
        # Using MLPY:
        # First, make sure deps are setup.
        # `brew install gsl`
        # Download from SF: http://mlpy.sourceforge.net/
        # Then install using setup.py:
        # `cd MLPY_PATH/setup.py install`

        # Now this makes it fun.
        x, y = random_timesequence(0, 10), random_timesequence(0, 10)

        # Taken from examples: http://mlpy.sourceforge.net/docs/3.5/dtw.html#id3
        distance, cost, path = mlpy.dtw_std(x, y, dist_only=False)
        fig = plot.figure(1)
        axes = fig.add_subplot(111)
        plot1 = plot.imshow(
            cost.T, origin='lower', cmap=cm.gray, interpolation='nearest')

        plot2 = plot.plot(path[0], path[1], 'w')
        bound = 0.5
        xlim = axes.set_xlim((-bound, cost.shape[0] - bound))
        ylim = axes.set_ylim((-bound, cost.shape[1] - bound))
        plot.show()
