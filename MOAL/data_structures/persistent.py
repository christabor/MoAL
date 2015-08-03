# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import print_simple
from MOAL.helpers.text import gibberish2
from datetime import datetime as dt

DEBUG = True if __name__ == '__main__' else False


class MutableAccessException:
    pass


class PersistentDataStructure(object):
    pass


class PartiallyPersistentNode(PersistentDataStructure):
    """From Wikipedia:

    "In computing, a persistent data structure is a data structure that always
    preserves the previous version of itself when it is modified.
    Such data structures are effectively immutable, as their operations do not
    (visibly) update the structure in-place,
    but instead always yield a new updated structure.

    A data structure is partially persistent if all versions can be accessed
    but only the newest version can be modified." """

    def __init__(self):
        self.versions = {}
        self.data = None

    def __str__(self):
        print('All data: {}').format(self.versions)
        print('Current data: {}'.format(self.data))
        return ''

    def __delitem__(self, key):
        """Deleting an item is not allowed, as the data structure
        should be immutable."""
        raise MutableAccessException

    def __setattr__(self, name, value):
        if name not in ['versions', 'data']:
            raise MutableAccessException
        super(PartiallyPersistentNode, self).__setattr__(name, value)

    def __setitem__(self, key, data):
        # Allow first value to be added, but do not allow subsequent overrides.
        if self.data is not None and key != self.data and key in self.versions:
            raise MutableAccessException
        # Add to history, then update.
        # If it is the current one, update the value.
        self.versions.update({key: data})
        # Keep reference to key only.
        self.data = key

    def view_all(self):
        print(self.versions)

    def get_current(self):
        return self.data

    def get_all(self):
        return self.versions


class FullyPersistentNode(PartiallyPersistentNode):
    """From Wikipedia:
    "The data structure is fully persistent if every version can be both
    accessed and modified." """

    def __setitem__(self, key, data):
        self.versions[key] = {'data': data}
        # Store a reference only, to the last modified element
        self.data = key

    def __getitem__(self, key):
        return self.versions[key]

    def get_current(self):
        return self.versions[self.data]


class ConfluentlyPersistentNode(FullyPersistentNode):
    """From Wikipedia:
    "If there is also a meld or merge operation that
    can create a new version from two previous versions,
    the data structure is called confluently persistent."  """

    def meld(self, key, versions=[]):
        print('Melding versions {versions} under key "{}"'.format(
            key, versions=versions))
        new = {}
        for version in versions:
            temp = self.__getitem__(version)['data']
            new.update(temp)
        self.__setitem__(key, new)


class ConfluentlyPersistentFatNode(ConfluentlyPersistentNode):
    """From Wikipedia:

    "Fat node method is to record all changes made to node fields in the nodes
    themselves, without erasing old values of the fields. This requires
    that we allow nodes to become arbitrarily 'fat'.

    Each extra field value has an associated field name and a version stamp
    which indicates the version in which the named field was changed to
    have the specified value.

    Besides, each fat node has its own version stamp, indicating the version
    in which the node was created. In order to navigate through the structure,
    each original field value in a node has a version stamp of zero." """

    def __setitem__(self, key, data):
        date = 0 if key not in self.versions else dt.now()
        _data = {'date_modified': date, 'data': data}
        # Add new key and versions container if it has never existed.
        if key not in self.versions:
            self.versions[key] = {'versions': [_data]}
        else:
            # Update current version inside of the specific node.
            self.versions[key]['versions'].append(_data)
        # Store a reference only, to the last modified element
        self.data = key

    def __getitem__(self, key):
        return self.versions[key]


class ConfluentlyPersistentPathCopyingNode(ConfluentlyPersistentNode):
    """TODO"""


class ConfluentlyPersistentPathCopyingFatNode(
        ConfluentlyPersistentFatNode, ConfluentlyPersistentPathCopyingNode):
    """TODO"""


if DEBUG:
    with Section('Persistent data structures'):

        print_h2('Persistent partial node')
        pnode = PartiallyPersistentNode()
        print(pnode)
        pnode['foo'] = {'foo': 'bar', 'bim': 'baz'}
        print(pnode)
        pnode.view_all()
        # Should work, as it's the single item and current.
        pnode['foo'] = [2, 3, 4, 5]
        # Should work, since it's new
        pnode['bar'] = [1, 2, 3]
        try:
            del pnode['bar']
        except MutableAccessException:
            pass
        try:
            # Should not work, since it exists,
            # and is no longer the current item.
            pnode['foo'] = {'foo': 'bar'}
        except MutableAccessException:
            print('Successfully blocked write of existing version.')

        print_h2('Persistent full node')
        pfatnode = FullyPersistentNode()
        # Updating and overriding existing data
        print(pfatnode)
        pfatnode['foo'] = {'bar': 'baz'}
        print(pfatnode)
        pfatnode['bar'] = {'baz': 'bar'}
        print(pfatnode)
        print_simple('Current fat node data', pfatnode.get_current())

        for _ in range(2):
            pfatnode[gibberish2()] = {gibberish2(): gibberish2()}
            print_simple('Fat node data', pfatnode.versions)

        print_h2('Persistent confluent')
        confluent = ConfluentlyPersistentNode()
        confluent['foo'] = {gibberish2(): gibberish2()}
        confluent['bar'] = {gibberish2(): gibberish2()}
        confluent['bim'] = {gibberish2(): gibberish2()}
        confluent['baz'] = {gibberish2(): gibberish2()}
        print_simple('Confluent node data', confluent.versions)

        confluent.meld('melded_example', versions=['foo', 'bar', 'baz', 'bim'])
        print_simple('Confluent node data', confluent.versions)

        print_h2('Persistent partial Fat Node')
        confluentfat = ConfluentlyPersistentFatNode()
        confluentfat['foo'] = {'_version': 1}
        confluentfat['bar'] = {'_version': 1}
        confluentfat['foo'] = {'_version': 2}
        confluentfat['foo'] = {'_version': 3}
        print_simple('Confluent fat node data', confluentfat.versions)

        ref = confluentfat.versions['foo']['versions']
        assert ref[0]['data']['_version'] == 1
        assert ref[1]['data']['_version'] == 2
        assert ref[2]['data']['_version'] == 3
