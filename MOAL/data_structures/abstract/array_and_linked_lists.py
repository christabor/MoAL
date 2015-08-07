# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.text import gibberish
from MOAL.helpers.display import cmd_title
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import prnt
from MOAL.helpers.display import print_simple
from MOAL.helpers import datamaker as dm
from faker import Factory
from random import shuffle

DEBUG = True if __name__ == '__main__' else False

faker = Factory.create()

# Arrays are simple: []. Nothing special here.

arr = []

# Python doesn't expose Linked Lists as usable data structures,
# so you can manually recreate the idea behind them using classes.


class SingleNode(object):

    def __init__(self, title, cargo=None, next=None):
        self.DEBUG = True
        self.title = title
        self.next = next
        self.cargo = cargo or gibberish(length=5)

    def __str__(self):
        return 'Node: {}'.format(self.__repr__())

    def __repr__(self):
        return '<_{title}_._{cargo}_>'.format(
            title=self.title, cargo=self.cargo)

    def __contains__(self, key):
        return self.__getitem__(key) is not None

    def __iter__(self):
        """Iterate over linked nodes"""
        node = self
        yield node
        while node.next is not None:
            node = node.next
            yield node

    def __setitem__(self, key, value):
        """Update the values of an existing node"""
        node = self.__getitem__(key)
        if node is not None:
            node.cargo = value

    def __getitem__(self, key):
        """Get an existing node"""
        node = self
        while node is not None:
            if node.title == key:
                return node
            node = node.next
        return None

    def last(self):
        """Move forward in the list until the last node is found
            e.g. [N] --> [N + 1] --> [N + 2]
        """
        next = self
        while next:
            if next.next is None:
                return next
            next = next.next
        return next

    def __len__(self):
        count = 1  # Inclusive, head is 0
        node = self
        while node.next is not None:
            count += 1
            node = node.next
        return count


class DoubleNode(SingleNode):
    """A node represents a connection in the linked list. This extends
    the single node (linked list) to become a doubly-linked list - a list with
    connections going in both directions (forward and backwards)."""

    def __init__(self, title, cargo=None, prev=None, next=None):
        super(DoubleNode, self).__init__(title, cargo=None, next=None)
        self.prev = prev

    def __delitem__(self, key):
        """Delete a node, purge any references, and update the adjacent links"""
        if self.title == key:
            node = self
        else:
            node = self.__getitem__(key)
        if node is None:
            return
        # Update linkage, e.g. (1) <-> 2 <-> (3) ... (1) <-> (3)
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if self.DEBUG:
            print('\nDELETING... {} {}'.format(node.title, node.cargo))
        del self[node.title]

    def first(self):
        """Move backward in the list until the first node is found
            e.g. [N - 2] <-- [N - 1] <-- [N]
        """
        prev = self
        while prev:
            if prev.prev is None:
                return prev
            prev = prev.prev
        return prev

    def prepend(self, key, value):
        """Add a new node to the very beginning of the list."""
        curr_begin = self.first()
        curr_begin.next = DoubleNode(title=key, cargo=value)
        curr_begin.next.prev = curr_begin

    def append(self, key, value):
        """Add a new node to the very end of the list."""
        curr_end = self.last()
        curr_end.next = DoubleNode(title=key, cargo=value)
        curr_end.next.prev = curr_end


def print_nodes(node):

    def _fmt(node):
        return '[<{}.{}>] {divider} '.format(
            node.title,
            node.cargo,
            divider='....' if node.next is not None else '') \
            if node is not None else ''
    path, count = '', 0
    cmd_title('Printing Nodes')
    # Follows a node along it's next target, until next is None.
    while node is not None:
        path += _fmt(node)
        count += 1
        node = node.next
    prnt('Linked List\n', path, newlines=False)


def build_list(length, head=None):
    if head is None:
        # Start from the beginning with a new node.
        head = DoubleNode('head', prev=None)
    curr_node = head
    curr = 0  # Head starts at 0
    while curr_node is not None:
        if curr == length - 1:
            title = 'tail'
        else:
            title = 'node-{}'.format(curr)
        if curr > 0:
            curr_node.title = title
        curr_node.next = None if (curr == length - 1) \
            else DoubleNode(title, prev=curr_node)
        # Advance to the next node, for the next iteration
        curr_node = curr_node.next
        curr += 1
    return head


class AssociationList(DoubleNode):
    """Our linked list already encapsulates all the behavior necessary.
    The required `key` and `value` properties are named `title` and `cargo`
    respectively. The association (lookup) can be evaluated by traversing the
    linked list and comparing the key, then returning the matching nodes value.

    This behavior is already done with the setter,
    so we don't need to re-define it here."""

    def __init__(self, *args, **kwargs):
        super(AssociationList, self).__init__(*args, **kwargs)

    def __getitem__(self, key):
        """Get an existing node, returning only the value."""
        node = self
        while node is not None:
            if node.title == key:
                return node
            node = node.next
        return None


if DEBUG:
    with Section('Arrays & Linked Lists'):
        MAX_NODES = 10
        single = SingleNode('head')
        single['next'] = SingleNode('next-1')
        print(single)

        linked_list = build_list(MAX_NODES)
        print_nodes(linked_list)
        prnt('Length of linked list:', len(linked_list), newlines=False)

        prnt('Testing iteration', '', newlines=False)
        for node in linked_list:
            print(node)

        del linked_list['node-1']
        del linked_list['node-4']
        del linked_list['node-2']
        del linked_list['node-6']
        del linked_list['tail']

        assert not linked_list['tail']

        prnt('Testing iteration - post delete:', '', newlines=False)

        for node in linked_list:
            print(node)

        linked_list['head'] = 'FOO'
        linked_list['node-3'] = 'BAR'
        linked_list['node-5'] = 'BIM'

        assert linked_list['head'].cargo == 'FOO'
        assert linked_list['node-3'].cargo == 'BAR'
        assert linked_list['node-5'].cargo == 'BIM'

        prnt('Testing value update', '', newlines=False)

        for node in linked_list:
            print(node)
            assert node.cargo

        print_h2('Parallel arrays')
        # "Parallel" arrays
        MAX_ITEMS = 10
        names = [faker.name() for _ in range(MAX_ITEMS)]
        emails = [faker.email() for _ in range(MAX_ITEMS)]
        parallel = [names, emails]
        for index in range(MAX_ITEMS):
            print('Name: {}, Email: {}'.format(names[index], emails[index]))

        print_h2('Matrix/Vector arrays')
        matrix = dm.random_matrix(rows=5, columns=5, choices=range(20))
        print_simple('Matrix', matrix)

        print_h2('Sorted array')
        # Props to John Neumann for "inventing" it
        orig = range(10)
        shuffle(orig)
        print('Shuffled: {}'.format(orig))
        print('Sorted: {}'.format(sorted(orig)))

        # Wikipedia glossary practice
        singleton = [1]
        not_singleton = [1, 2]
