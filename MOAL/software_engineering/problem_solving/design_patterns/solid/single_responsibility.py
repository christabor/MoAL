# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


DEBUG = True if __name__ == '__main__' else False

# Multiple responsibility...


class SwissArmyKnife:
    """...What exactly is this for, again?"""

    def cut(self, blade='medium'):
        pass

    def open_wine(self):
        pass

    def scissor(self):
        pass

    def file(self):
        pass

    def magnify(self):
        pass

    def saw(self):
        pass

    def tweeze(self):
        pass

    def screw(self, type='phillips'):
        pass

    def unscrew(self, type='phillips'):
        pass


# Single responsibility

class ScrewDriver:

    def unscrew(self, degrees=90):
        pass

    def screw(self, degrees=90):
        pass


class Phillips(ScrewDriver):
    pass


class FlatHead(ScrewDriver):
    pass


class Hex(ScrewDriver):
    pass


class Corkscrew:

    def open_wine(self):
        pass


class Blade:

    def cut(self):
        pass


class SerratedKnife(Blade):
    pass


class LargeBlade(Blade):
    pass


class SmallBlade(Blade):
    pass


class Saw:
    pass


class Scissor:
    pass
