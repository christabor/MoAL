# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
import inspect
import abc


class Life(object):
    """The new-style base class for all living things."""


class Domain(Life):

    def __init__(self):
        super(Domain, self).__init__()


class Kingdom(Domain):

    def __init__(self):
        super(Kingdom, self).__init__()


class Phylum(Kingdom):

    def __init__(self):
        super(Phylum, self).__init__()


class Class(Phylum):

    def __init__(self):
        super(Class, self).__init__()


class Order(Class):

    def __init__(self):
        super(Order, self).__init__()


class Family(Order):

    def __init__(self):
        super(Family, self).__init__()


class Genus(Family):

    def __init__(self):
        super(Genus, self).__init__()


class Species(Genus):

    def __init__(self):
        super(Species, self).__init__()

"""
    Extensions beyond the global biological classification

"""


class AbstractCat(Family):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def custom_abstractmethod(self):
        """This is an abstract method."""


class AbstractCatTwo(Family):

    def __init__(self):
        pass

    def custom_abstractmethod(self):
        raise NotImplementedError


class Cat(AbstractCat):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'My name is `{}`'.format(self.name)

    def __hash__(self):
        return len(self.name)

    def custom_abstractmethod(self):
        return 'Abstract method override'

    @staticmethod
    def custom_staticmethod():
        return 'I am a static method with no instance.'

    @classmethod
    def custom_classmethod(cls):
        return 'I am a class method.'

    @classmethod
    def meow(cls):
        return 'Meowwwww'


class CatTwo(AbstractCatTwo):
    pass


"""
    Second derived classes from first derived
    biological classification classes.

"""


class HouseCat(Cat):

    def __init__(self, name):
        super(HouseCat, self).__init__(name)


class InernetHouseCats(HouseCat):
    pass


class Maru(InernetHouseCats):

    def box_attack(self):
        pass


class Grumpy(InernetHouseCats):

    def frown(self):
        pass


class ColonelMeow(InernetHouseCats):

    def attack(self):
        pass


"""
    Class methods example
"""

if __name__ == '__main__':
    with Section('OOP Class types / examples'):
        print
        print Cat.meow()
        print Cat.custom_classmethod()
        print Cat.custom_classmethod
        print

        """
            Examples of actual usage of class instances
        """

        classes = ' <= '.join([c.__name__ for c in inspect.getmro(Species)])
        print 'Classes for most derived class {} are: {}'.format(
            Species, classes)

        leopard = Cat('leopard')
        print repr(leopard)

        calico = HouseCat('calico')
        print calico.meow()
        print repr(calico)

        print 'Classmethod: {}'.format(Cat.custom_classmethod())
        print Cat.custom_classmethod
        print 'Staticmethod: {}'.format(Cat.custom_staticmethod())
        print Cat.custom_staticmethod
        print 'Staticmethod instance: {}'.format(leopard.custom_staticmethod())
        print 'Comparison: {} {} {}'.format(
            leopard, calico, (hash(leopard) == hash(calico)))
        print
        abstract_leopard = CatTwo()

        # Not implement error
        try:
            print abstract_leopard.custom_abstractmethod
            abstract_leopard.custom_abstractmethod()
        except NotImplementedError:
            print ('This exception is an example of the second '
                   'abstract method strategy: simply raising a NotImplemented'
                   'exception rather than going through the rigamorale of '
                   'using a traditional ABC decorator.')
        print
