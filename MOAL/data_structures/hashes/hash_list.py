# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.text import gibberish3
from MOAL.helpers.display import Section
from MOAL.data_structures.hashes.hashtable import NaiveHashTable
from pprint import pprint as ppr


DEBUG = True if __name__ == '__main__' else False


class HashList(NaiveHashTable):
    """Stores a list of computed hashes for each block of data (specified
    by offset) for a given string block representing a file-like object."""

    def __init__(self, filedata, chunk_size=4):
        super(HashList, self).__init__()
        self.hash_list = []
        self.compute_hashes(filedata, chunk_size)

    def __str__(self):
        ppr(self.hash_list)
        return ''

    def hash(self, data):
        return self.hash_fnv1a(data)

    def compute_hashes(self, filedata, chunk_size):
        """Compute a list of hashes for each block of data given by `filedata`.
        Chunk size will affect performance since each chunk has to be hashed.
        This is largely dependent on the hashing algorithm used.
        """
        current_offset = 0
        while len(filedata) > 0:
            # Add hashed chunk to the list
            self.hash_list.append(
                self.hash(filedata[current_offset:]))
            current_offset += chunk_size
            # Continue with substring value
            filedata = filedata[current_offset:]


class MockFile:

    def __init__(self):
        self.data = ''.join(map(gibberish3, range(10)))

    def __str__(self):
        return self.data

if DEBUG:
    with Section('Hash list'):
        fakefile = MockFile()
        hashlist = HashList(fakefile.data, chunk_size=12)
        print(hashlist)
