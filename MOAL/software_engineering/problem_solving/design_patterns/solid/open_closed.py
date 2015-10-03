# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


from MOAL.helpers.display import Section
from abc import ABCMeta, abstractmethod

DEBUG = True if __name__ == '__main__' else False


# Some good counter-examples and/or debate:
# http://c2.com/cgi/wiki?OpenClosedPrinciple

class ConnectionManagerABC:
    """The essence of the Open/Closed principle is that objects should be
    open for extension but closed for modification. This is effectively
    what an abstract base class (or virtual interface) provides, because
    it requires anything that uses it to extend from it, rather than
    changing it directly. In Python the ABC module will enforce this
    principle by checking that all subclassed methods provide an overriding
    method if the deriving class has an abstractmethod set."""

    __metaclass__ = ABCMeta
    ips = {}

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def drop(self):
        pass


class ConnectionManager(ConnectionManagerABC):
    """Valid, since it extends the methods."""

    def add(self, ip):
        self.ips[ip] = True

    def drop(self, ip):
        del self.ips[ip]


class DistributedConnectionManager(ConnectionManagerABC):
    """Invalid, since it doesn't extend the methods."""


if DEBUG:
    with Section('SOLID - Open/Closed principle'):
        conn = ConnectionManager()
        try:
            dconn = DistributedConnectionManager()
        except TypeError:
            print('Successfully prevented incomplete class from being created.')
