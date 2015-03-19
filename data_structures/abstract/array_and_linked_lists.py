# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.text import gibberish
from helpers.display import _cmd_title
from helpers.display import prnt

DEBUG = True if __name__ == '__main__' else False

# Arrays are simple: []. Nothing special here.

arr = []

# Python doesn't expose Linked Lists as usable data structures,
# so you can manually recreate the idea behind them using classes.


class LinkNode(object):
    """A node represents a connection in the linked list."""

    def __init__(self, title, cargo=None, prev=None, next=None):
        self.DEBUG = True
        self.title = title
        self.next = next
        self.prev = prev
        self.cargo = cargo or gibberish(length=5)

    def __str__(self):
        return 'Node: {}'.format(self.__repr__())

    def __repr__(self):
        return '<_{title}_._{cargo}_>'.format(
            title=self.title, cargo=self.cargo)

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

    def __delitem__(self, key):
        """Delete a node, purge any references, and update the adjacent links"""
        if self.title == key:
            node = self
        else:
            node = self.__getitem__(key)
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if self.DEBUG:
            print('\nDELETING... {} {}'.format(node.title, node.cargo))
        del node

    def __len__(self):
        count = 1  # Inclusive, head is 0
        node = self
        while node.next is not None:
            count += 1
            node = node.next
        return count

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

    def prepend(self, key, value):
        """Add a new node to the very beginning of the list."""
        curr_begin = self.first()
        curr_begin.next = LinkNode(title=key, cargo=value)
        curr_begin.next.prev = curr_begin

    def append(self, key, value):
        """Add a new node to the very end of the list."""
        curr_end = self.last()
        curr_end.next = LinkNode(title=key, cargo=value)
        curr_end.next.prev = curr_end


def print_nodes(node):

    def _fmt(node):
        return '[<{}.{}>] {divider} '.format(
            node.title,
            node.cargo,
            divider='....' if node.next is not None else '') \
            if node is not None else ''
    path, count = '', 0
    _cmd_title('Printing Nodes')
    # Follows a node along it's next target, until next is None.
    while node is not None:
        path += _fmt(node)
        count += 1
        node = node.next
    prnt('Linked List\n', path)


def build_list(length, head=None):
    if head is None:
        # Start from the beginning with a new node.
        head = LinkNode('head', prev=None)
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
            else LinkNode(title, prev=curr_node)

        # Advance to the next node, for the next iteration
        curr_node = curr_node.next
        curr += 1
    return head


class AssociationList(LinkNode):
    """Our linked list already encapsulates all the behavior necessary.
    The required `key` and `value` properties are named `title` and `cargo`
    respectively. The association (lookup) can be evaluated by traversing the
    linked list and comparing the key, then returning the matching nodes value.

    This behavior is already done with the setter, but to be explicit,
    we'll re-define a method that returns ONLY the value,
    rather than the entire node reference."""

    def __init__(self, *args, **kwargs):
        super(AssociationList, self).__init__(*args, **kwargs)

    def __getitem__(self, key):
        """Get an existing node, returning only the value."""
        node = self
        while node is not None:
            if node.title == key:
                return node.cargo
            node = node.next
        return None

    def __setitem__(self, *args, **kwargs):
        return self.append(*args, **kwargs)

if DEBUG:
    with Section('Arrays & Linked Lists'):
        MAX_NODES = 10
        linked_list = build_list(MAX_NODES)
        print_nodes(linked_list)
        prnt('Length of linked list:', len(linked_list))

        prnt('Testing iteration', '')
        for node in linked_list:
            print(node)

        del linked_list['node-1']
        del linked_list['node-4']
        del linked_list['node-2']
        del linked_list['node-6']
        del linked_list['tail']

        prnt('Testing iteration - post delete:', '')

        for node in linked_list:
            print(node)

        linked_list['head'] = 'FOO'
        linked_list['node-3'] = 'BAR'
        linked_list['node-5'] = 'BIM'

        prnt('Testing value update', '')

        for node in linked_list:
            print(node)

# Glossary practice

singleton = [1]
not_singleton = [1, 2]
