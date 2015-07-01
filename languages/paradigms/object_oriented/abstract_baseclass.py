# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from abc import abstractproperty
from abc import abstractmethod
from abc import ABCMeta

DEBUG = True if __name__ == '__main__' else False


class MyAbstractThing:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_items(self):
        print('Hello from ABC!')

    @abstractproperty
    def get_user(self):
        """Get user properties."""
        return self.user


class MyBrokenConcreteThing(MyAbstractThing):

    def _get_items(self):
        """This method is named slightly different, meaning it won't override
        the abstract base class, which will cause a failure."""


class MyConcreteThing(MyAbstractThing):

    def get_items(self):
        super(MyConcreteThing, self).get_items()
        print('Overriden after ABC')

    @property
    def get_user(self):
        """Get user properties."""
        return self.user

    @classmethod
    def get_some_stuff(cls):
        pass


if DEBUG:
    with Section('Abstract Base Classes'):
        assert not issubclass(MyAbstractThing, ABCMeta)
        assert issubclass(MyConcreteThing, MyAbstractThing)

        print('type', type(MyAbstractThing))
        print('type', type(MyConcreteThing))
        print(MyAbstractThing, MyConcreteThing)

        try:
            print(MyAbstractThing())
        except TypeError:
            print('Abstract methods on abstract '
                  'classes are not meant to be instantiated.')

        try:
            print(MyBrokenConcreteThing())
        except TypeError:
            print('Abstract class derived classes require all '
                  'abstract methods to be overriden.')

        # Hooray!
        print(MyConcreteThing())
        concr = MyConcreteThing()
        concr.get_items()
