# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import print_h3
from MOAL.helpers.display import print_info
from MOAL.helpers.display import divider
from MOAL.helpers.text import randchars
from MOAL.data_structures.abstract.array_and_linked_lists import AssociationList
from random import randrange as rr
from random import choice
from faker import Factory

DEBUG = True if __name__ == '__main__' else False


class MapADT(AssociationList):
    """From wikipedia.org/wiki/Associative_array:

    Operations associated with this data type allow:
        * The addition of pairs to the collection
        * The removal of pairs from the collection
        * The modification of the values of existing pairs
        * The lookup of the value associated with a particular key

    ----------------------------------------------------------------------

    While we could just use a dictionary (cheating), it would make sense
    to use a vanilla array and implement a custom & importantly, internal,
    function that does key lookups.

    However, an associative array / map is purely abstract, and other data types
    use it as a template, either concretely or conceptually. A linked list is
    given as an example implementation, so we can use it here,
    providing some basic methods that act as a facade pattern over the
    internal implementation."""

    def __str__(self):
        print('{')
        for node in self:
            print(' "{}": "{}",'.format(node.title, node.cargo))
        print('}')
        return ''


class MultiMap(MapADT):
    """From wikipedia.org/wiki/Multimap (paraphrased):
    "In computer science, a multimap (sometimes also multihash) is a
    generalization of a map or associative array abstract data type in which
    more than one value may be associated with and returned for a given key.

    Often the multimap is implemented as a map with lists/sets as the values."

    "Both map and multimap are particular cases of containers"
    (See abstract/container for an example of this ADT.)

    Since our MapADT uses a linked list, and the linked list implementation
    does not prohibit certain types as values,
    we can simply use a list as mentioned above for the value.

    We could enforce certain types on the original linked list,
    but that is arbitrary and unnecessary."""

    def __setitem__(self, key, value):
        super(MultiMap, self).append(key, value)


class Enrollment(MultiMap):

    def __init__(self, students=[], classes=[], title='Enrollment-MultiMap'):
        self.MAX_CLASSES = 4
        self.classes = classes
        self.students = students
        super(Enrollment, self).__init__(title=title)

    def enroll(self, student, klass):
        super(Enrollment, self).__setitem__(student, klass)

    def enroll_all(self, schedules):
        for student, classes in schedules.iteritems():
            for klass in classes:
                self.enroll(student, klass)
        if DEBUG:
            divider(atom='.')

    def _classes(self):
        return [choice(self.classes) for _ in range(self.MAX_CLASSES)]

    def schedules(self):
        self.schedules = [{
            student: self._classes()} for student in self.students]
        return self.schedules

    def get_classes(self, student):
        res = super(Enrollment, self).__getitem__(student)
        classes = res.cargo
        return classes

    def __setitem__(self, student, klass):
        # Toss in a random class level (e.g 101, 302)
        klass = '{}{} {}'.format(choice(['AP ', '']), klass, str(rr(100, 999)))
        if DEBUG:
            print('Enrolling {} into {}'.format(student, klass))
        super(Enrollment, self).__setitem__(student, klass)


class BidirectionalMap(dict):
    """The bi-directional map uses a dictionary rather than an associative
    or linked list, since the main purposes is to stress the concept of
    bi-directional mapping, not the actual implementation. Besides, a dict would
    be a better implementation for real-world usage, at least in python."""

    def __str__(self):
        print('{')
        for key, val in self.items.iteritems():
            print('  {}: {}'.format(key, val))
            # print('  {}: {} (or) {}: {}'.format(key, val, val, key))
        print('}')
        return ''

    def __init__(self, *args, **kwargs):
        self.items = {}
        self.items.update(*args, **kwargs)

    def __contains__(self, key):
        for _key, val in self.items.iteritems():
            if _key == key:
                return True
            elif val == key:
                return True
        return False

    def __getitem__(self, key, value):
        try:
            return self[key]
        except KeyError:
            return self[value]
        finally:
            pass

    def __setitem__(self, key, val):
        """The idea here is that a key and a value are interchangeable,
        but either direction should still enforce the rules of a traditional
        map (or dictionary, in this case.)"""
        keys = self.items.keys()
        values = self.items.values()
        is_both_key = key in keys and key in values
        is_both_val = val in keys and val in values
        if is_both_key or is_both_val:
            raise ValueError(
                'Item already exists in both key and value'
                ' -- it can only exist in one!')
        super(BidirectionalMap, self).__setitem__(key, val)


if DEBUG:
    with Section('Map Abstract Data Type'):
        map_adt = MapADT(title='map_head')

        for n in range(6):
            key = 'map_item-{}'.format(''.join(randchars(8)))
            map_adt[key] = ''.join(randchars(4))

        print(map_adt)

    with Section('Multi-Map Abstract Data Type'):
        faker = Factory.create()
        multimap = MultiMap(title='multi-map_head')

        print_h2('Multimap', desc='General abstract usage.')

        for n in range(4):
            key = 'map_item-{}'.format(n)
            multimap[key] = ''.join(randchars(4))

        print(multimap)
        print(multimap['map_item-1'])

        print_h2('Multimap', desc='Used contextually for school enrollment.')

        classes_map = Enrollment(
            classes=['English', 'Comp Sci', 'History', 'Math', 'Art'],
            students=[faker.name() for _ in range(3)] + ['Ms. Ella Tabor'])

        map(classes_map.enroll_all, classes_map.schedules())
        print_h3('All fields')

        print(classes_map)

        print_h3('\nClasses for Ella Tabor')
        print('Classes: {}'.format(classes_map.get_classes('Ms. Ella Tabor')))

        del classes_map['Ms. Ella Tabor']

        # Too young to be taking classes right now anyway.
        assert classes_map['Ms. Ella Tabor'] is None

        print(classes_map)

        assert 'Ms. Ella Tabor' not in classes_map

        print_h3('Bi-directional', desc='A map ADT that maps to key OR value.')

        bdmap = BidirectionalMap(
            {1: 'Foo', 2: 'Bar', 'Foo': 'Bar', 'Bar': 'Foo'})
        print(bdmap)
        try:
            bdmap['Bar'] = 'Foo'
            bdmap['Foo'] = 'Bar'
        except ValueError:
            print_info('Test raising error for duplicate values Foo and Bar')
        print(bdmap)
        assert 'Bar' in bdmap
        assert 'Foo' in bdmap
