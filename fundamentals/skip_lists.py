# -*- coding: utf-8 -*-

# Based on code from
# https://kunigami.wordpress.com/2012/09/25/skip-lists-in-python/

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from random import randrange as rr
from generic_helpers import _gibberish
from generic_helpers import section


class SkipNode:

    def __init__(self, height=0, elem=None):
        self.elem = elem
        # This usually results in a default to
        # zero when initializing the first node.
        self.height = height
        self.next = [None] * self.height

    def view(self):
        res = ''
        for el in self.next:
            res += '[{}] --> '.format(el.elem['value'] if el is not None else el)
        print res


class SkipList:

    def __init__(self):
        self.head = SkipNode()

    def random_height(self):
        return rr(1, 10)

    def update_list(self, elem):
        # Get a copy of the next list, but as empty NoneType values
        updated = [None] * len(self.head.next)
        # Copy the head into a new variable
        x = self.head
        # Reverse and go over the original list while
        # there are actual elements, filling in the updatedd copy by swapping
        # the nodes with each pass.
        # for i, el in enumerate(reversed(self.head.next)):
        for i in reversed(range(len(self.head.next))):
            while x.next[i] is not None and x.next[i].elem['value'] < elem['value']:
                # Continue updating x to the next grater elements' index
                x = x.next[i]
            updated[i] = x
        return updated

    def view(self):
        print 'Viewing entire skip list:'
        for node in self.head.next:
            print self.head.elem, '-->', node.view()

    def find(self, elem, updated=None):
        """Finds an item in the list. Allows the optional `updated`
        flag to be passed in, which represents an updated
        copy to search from instead."""

        # If updated is none, updated the list and retry.
        if updated is None:
            updated = self.update_list(elem)
        # Only try if the list is > 0
        # Return None if not found, otherwise return the first index
        # of the next pointer.
        if len(updated) > 0:
            candidate = updated[0].next[0]
            if candidate is not None and candidate.elem is elem:
                return candidate
        return None

    def remove(self, elem):
        updated = self.update_list(elem)
        x = self.find(elem, updated=updated)
        # Remove only if it's not None -- since None represents
        # an empty element (since by default all spaces are fill with None)
        if x is not None:
            for i, _ in enumerate(x.next):
                # Nullify the matching pointer
                updated[i].next[i] = x.next[i]
                # Left unchanged for now, but cleanup can be done
                if self.head.next[i] is None:
                    continue

    def _balance_length(self, node):
        # Keep adding None elements until the the length of
        # each list is equal and thus the lists are balanced.
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

    def insert(self, elem):
        # Create a new node with random height
        node = SkipNode(height=self.random_height(), elem=elem)
        print 'Adding {} node to the list:'.format(elem)

        # Balance length before inserting to avoid issues with indices.
        self._balance_length(node)
        updated = self.update_list(elem)
        # Add the new element if it doesn't already exist.
        if self.find(elem, updated=updated) is None:
            for i, _ in enumerate(node.next):
                node.next[i] = updated[i].next[i]
                updated[i].next[i] = node


section('BEGIN - Skip Lists')

gibs = [{'name': _gibberish(), 'value': rr(10, 1000)} for _ in range(10)]
sl = SkipList()
for gib in gibs:
    sl.insert(elem=gib)

for gib in gibs:
    sl.find(gib)

sl.view()

section('END - Skip Lists')
