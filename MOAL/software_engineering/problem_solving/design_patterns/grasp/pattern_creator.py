# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class AbstractVehicle:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'I am a {}'.format(self.name)


class Automobile(AbstractVehicle):
    pass


class Plane(AbstractVehicle):
    pass


class Train(AbstractVehicle):
    pass


class ClassFactory:

    @staticmethod
    def make(name, instantiate=False):
        newcls = None
        if name is 'car' or name is 'automobile':
            newcls = Automobile
        elif name is 'plane':
            newcls = Plane
        elif name is 'train':
            newcls = Train

        if newcls is None:
            raise ValueError('Invalid class.')
        if instantiate:
            return newcls(name)
        else:
            return newcls


if DEBUG:
    with Section('GRASP Factory/Creator pattern'):
        clstypes = [('car', Automobile), ('plane', Plane), ('train', Train)]
        for clstype in clstypes:
            _cls, real_class = clstype
            output = ClassFactory.make(_cls)
            assert not isinstance(output, real_class)

            _cls, real_class = clstype
            output = ClassFactory.make(_cls, instantiate=True)
            assert isinstance(output, real_class)
            print('Created new `{}` from {}'.format(_cls, real_class))
            print(_cls)
