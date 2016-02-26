"""Manhattan Distance algorithm."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from random import randrange

DEBUG = True if __name__ == '__main__' else False


def manhattan_distance(p1, p2):
    """Compute manhattan distance.

    Args:
        p1 (dict): The x and y coordinates of point 1
        p2 (dict): The x and y coordinates of point 2

    Returns:
        int: The calculated distance.
    """
    # Equation from https://xlinux.nist.gov/dads//HTML/manhattanDistance.html
    # it is |x1 - x2| + |y1 - y2|.
    return abs(p1['x'] - p2['x']) + abs(p1['y'] - p2['y'])


def rand_coords(max_width=100, max_height=100):
    """Generate random coordinates."""
    return {'x': randrange(0, max_width), 'y': randrange(0, max_height)}


if DEBUG:
    with Section('SOME MODULE TITLE'):
        c1 = [rand_coords() for _ in range(10)]
        c2 = [rand_coords() for _ in range(10)]
        for p1, p2 in zip(c1, c2):
            dist = manhattan_distance(p1, p2)
            print('Distance for {} and {} = {}'.format(p1, p2, dist))
