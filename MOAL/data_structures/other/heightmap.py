# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

DEBUG = True if __name__ == '__main__' else False


class HeightMap:
    """A heightmap is a data structure used to store the height values of
    (typically) a terrain geometry in 3-d programs.

    Each value may represent discrete sections across the terrain grid."""

    def __init__(self, size=10, max=10):
        self.max = float(max)
        self.size = float(size)

    def get_data(self, ztype='sin'):
        """Return data format suitable for plotting."""
        x = np.arange(-self.size, self.size, self.size // 4)
        y = np.arange(-self.max, self.max, self.max // 4)
        x, y = np.meshgrid(x, y)
        if ztype == 'sin':
            func = np.sin
        elif ztype == 'cos':
            func = np.cos
        else:
            func = np.tan
        z = func(np.sqrt(x ** 2 + y ** 2))
        return (x, y, z)


if DEBUG:
    with Section('HeightMap - 3d terrain'):
        height_map = HeightMap()
        fig = plt.figure()
        ax3d = fig.gca(projection='3d')
        ax3d.plot_surface(*height_map.get_data(),
                          rstride=2, cstride=2, linewidth=0, shade=True)
        plt.show()
