# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

# Arrays are simple: []. Nothing special here.

arr = []

# Python doesn't have Linked Lists in the traditional sense,
# so you can manually recreate the idea behind them using classes.

from helpers.display import Section
from helpers.text import gibberish
from helpers.display import _cmd_title
from helpers.display import prnt


class Node:
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
        node = self
        yield node
        while node.next is not None:
            node = node.next
            yield node

    def __setitem__(self, key, value):
        node = self.__getitem__(key)
        if node is not None:
            node.cargo = value

    def __getitem__(self, key):
        node = self
        while node is not None:
            if node.title == key:
                return node
            node = node.next
        return node

    def __delitem__(self, key):
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


def build_list(length):
    # Start from the beginning with a new node.
    head = Node('head', prev=None)
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
            else Node(title, prev=curr_node)

        # Advance to the next node, for the next iteration
        curr_node = curr_node.next
        curr += 1
    return head


if __name__ == '__main__':
    with Section('Arrays & Linked Lists'):
        DEBUG = True
        MAX_NODES = 10
        linked_list = build_list(MAX_NODES)
        print_nodes(linked_list)
        prnt('Length of linked list:', len(linked_list))

        if DEBUG:
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
