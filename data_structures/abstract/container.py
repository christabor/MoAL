# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from helpers.text import randchars
from pprint import pprint as ppr


class ContainerADT(object):
    """
    From wikipedia.org/wiki/Container_%28abstract_data_type%29:
    "
    Container classes are expected to implement methods to do the following:
        * create a new empty container,
        * report the number of objects it stores (size),
        * delete all the objects in the container (clear),
        * insert new objects into the container,
        * remove objects from it,
        * provide access to the stored objects.
        * containers are sometimes implemented in conjunction with iterators.
    "
    """
    def __init__(self):
        self.elements = {}
        print('<Constructor for container>')

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        for el in self:
            print('el', el, self[el])
        return ''

    def __contains__(self, element):
        return element in self.elements

    def __iter__(self):
        return iter(self.elements)

    def __delitem__(self, key):
        del self.elements[key]

    def __setitem__(self, key, value):
        self.elements[key] = value

    def __getitem__(self, key):
        return self.elements[key]

    @staticmethod
    def new(self, *args, **kwargs):
        self.__init__(self, *args, **kwargs)

    def size(self):
        self.__len__()

    def clear(self):
        self.elements = {}

    def insert(self, key, value):
        self.__setitem__(key, value)

    def remove(self, key, value):
        self.__delitem__(key, value)

    def access(self, key):
        return self.__getitem__(key)


class ValueContainer(ContainerADT):
    """
    [Wikipedia]
    "Store copies of objects. If we access an object, the object returns
    a copy of it. If an external object is changed after it has been inserted
    in the container it will not affect the content of the container."
    """


class ReferenceContainer(ContainerADT):
    """
    [Wikipedia]
    "
    Store pointers or references to the object.
    If we access an object, the object returns a reference to it.
    If an external object is changed after it has been inserted in
    the container, it affects the content of the container.
    "
    """


class WindowWidget(ReferenceContainer):
    """See wikipedia.org/wiki/Container_%28abstract_data_type%29
    ... "Graphic containers" as inspiration.
    """

    def __init__(self, name):
        super(WindowWidget, self).__init__()
        self.name = name

    def __str__(self):
        print('======== Viewing the widget "{}" =========\n'.format(self.name))
        for k in self.elements:
            print('[Widget {} ----->'.format(
                self.elements[k].name), self.elements[k])
        return ''

    def attach(self, *args, **kwargs):
        super(WindowWidget, self).__setitem__(*args, **kwargs)

    def detach(self, *args, **kwargs):
        super(WindowWidget, self).__delitem__(*args, **kwargs)

    def retrieve(self, *args, **kwargs):
        return super(WindowWidget, self).__getitem__(*args, **kwargs)

    def show(self):
        self.__str__()


if __name__ == '__main__':
    with Section('Container Abstract Data Type'):
        val_cont = ContainerADT()
        for n in range(4):
            val_cont[n * n] = randchars(n)
            val_cont.insert(n, randchars(n))
        print(val_cont.size())
        print(val_cont.new('fooo'))

        for el in val_cont:
            print('Iterator: {}, membership check ({}) => {}'.format(
                val_cont[el], el, el in val_cont))

        prnt('Value Container', val_cont.elements)

        print(val_cont.clear())
        prnt('Empty Container', val_cont.elements)
        assert len(val_cont) == 0

        ref_cont = ReferenceContainer()

        prnt('Reference Container...', ref_cont)

        meta = ReferenceContainer()
        ref_cont.insert('meta', meta)
        ppr(ref_cont.elements)

        # Change original instance
        meta['foo'] = 'bar'
        print(ref_cont.elements['meta'].elements)
        print(ref_cont)
        # Reference is also updated.
        ppr(ref_cont.elements['meta'].elements == meta.elements)

        # Examples of usage/extension
        desktop = WindowWidget('MyComputer')
        desktop.attach('Toolbar', WindowWidget('toolbar-01'))
        desktop.attach('Navigation', WindowWidget('navbar-01'))
        print(desktop.retrieve('Toolbar'))
        desktop.show()
