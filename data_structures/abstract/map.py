# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.text import randchars
from data_structures.abstract.array_and_linked_lists import AssociationList

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


if __name__ == '__main__':
    with Section('Map Abstract Data Type'):
        map_adt = MapADT(title='map_head')

        for n in range(30):
            key = 'map_item-{}'.format(''.join(randchars(8)))
            map_adt[key] = ''.join(randchars(4))

        print(map_adt)
