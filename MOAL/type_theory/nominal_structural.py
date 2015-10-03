# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from inspect import getmembers
from inspect import isdatadescriptor
from inspect import ismethod
from abc import ABCMeta

DEBUG = True if __name__ == '__main__' else False


class TesterMixin:

    def show_class(self):
        print(self.__class__)


class PrimaryNominal(object, TesterMixin):
    pass


class SubNominal(PrimaryNominal):
    pass


class StructuralType(object, TesterMixin):

    __metaclass__ = ABCMeta
    debug = True

    @staticmethod
    def compare(self_methods, self_props, other_methods, other_props):
        string = 'Self methods/props: {}, {} | Other methods/props: {}, {}'
        print(string.format(
            self_methods, self_props, other_methods, other_props))

    @staticmethod
    def _extract_props(cls):
        return map(lambda e: e[0], getmembers(cls, predicate=isdatadescriptor))

    @staticmethod
    def _extract_members(cls):
        return map(lambda e: e[0], getmembers(cls, predicate=ismethod))

    @classmethod
    def __subclasshook__(cls, subclass):
        """Use an abc and override subclass hook by looking
        over all the methods and properties of the class. This allows for
        structural comparison, instead of the typical inheritance pattern."""

        # stackoverflow.com/questions/1911281/
        #   how-do-i-get-list-of-methods-in-a-python-class
        self_methods = StructuralType._extract_members(cls)
        other_methods = StructuralType._extract_members(subclass)
        self_props = StructuralType._extract_props(cls)
        other_props = StructuralType._extract_props(subclass)
        if cls.debug:
            cls.compare(self_methods, self_props, other_methods, other_props)
        if self_methods == other_methods and self_props == other_props:
            return True
        return False

    def test_method(self):
        raise NotImplementedError


class ValidSubStructuralType(StructuralType):

    def test_method(self, *args):
        print(args)


class InvalidSubstructuralType(StructuralType):

    random_other_prop = 'Foobar'

    def test_method_2(self, *args):
        print(args)


if DEBUG:
    with Section('Nominal type system'):
        # Python is inherently nominal -- classes extend based on explicit
        # class declarations, and are then checked by the internal
        # Method Resolution Order.
        prim = PrimaryNominal()
        prim.show_class()

        sub = SubNominal()
        sub.show_class()

        # Fine and dandy, typical behavior.
        assert issubclass(SubNominal, PrimaryNominal)

    with Section('Structural type system'):
        try:
            # Should not work, with invalid sub-structural type checking.
            assert issubclass(StructuralType, InvalidSubstructuralType)
        except AssertionError:
            print('Successfully failed, type is not valid, structurally.')

        StructuralType.register(InvalidSubstructuralType)
        StructuralType.register(ValidSubStructuralType)

        # Should work, with valid sub-structural type checking.
        assert not issubclass(InvalidSubstructuralType, StructuralType)
        assert issubclass(ValidSubStructuralType, StructuralType)
