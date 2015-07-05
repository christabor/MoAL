# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from uuid import uuid1
from random import choice
from random import randrange as rr

DEBUG = True if __name__ == '__main__' else False


class MonitorDB:

    def __init__(self):
        self.store = {}

    def __setitem__(self, id, data):
        self.store[id] = data


class GridMonitorService:
    """This monitor service acts as an intermediary for handling db and object
    related functionality, and can be used to continually add more utilities
    that are related to the single entity, but that shouldn't be stored
    directly on it.

    It can be though of as a service-like layer of indirection:

    entity <------> entity_service <------> data-store

    """

    def __init__(self, grid):
        self.data = MonitorDB()
        self.grid = grid

    def check_status(self):
        for id, light in self.grid.lights.iteritems():
            print('Light #{} is currently: {} @ x:{} y:{} z:{}'.format(
                id, light.status(), *light.coords))


class Monitor:

    def on(self):
        self.on = True

    def off(self):
        self.off = False

    def status(self):
        return 'ON' if self.on else 'OFF'


class LightMonitor(Monitor):

    def __init__(self, coords):
        self.coords = coords
        # For fun
        self.on = choice([True, False])


class LightGrid:

    def __init__(self):
        self.lights = {}

    def __setitem__(self, id, coords):
        self.lights[id] = LightMonitor(coords)


if DEBUG:
    with Section('GRASP pure fabrication pattern'):
        grid = LightGrid()
        gridmon = GridMonitorService(grid)

        for _ in xrange(10):
            grid[uuid1()] = (rr(0, 1000), rr(0, 1000), rr(0, 1000))

        gridmon.check_status()
