# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# Arrays are simple: []. Nothing special here.

arr = []

# Python doesn't have Linked Lists in the traditional sense,
# so you can manually recreate the idea behind them using classes.
# http://greenteapress.com/thinkpython/html/chap17.html is a great resource
# for understanding all the fundamentals and how to use/access/create
# a linked list and will be the primary source of inspiration here...

from generic_helpers import Section
from generic_helpers import _gibberish
from generic_helpers import _cmd_title
from generic_helpers import _print


class Node:
    """A node represents a connection in the linked list."""

    def __init__(self, title, cargo=None, prev=None, next=None):
        self.DEBUG = True
        self.title = title
        self.next = next
        self.prev = prev
        self.cargo = cargo or _gibberish(length=5)

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

    def __getitem__(self, key):
        if self.title == key:
            return self
        node = self
        while node is not None:
            if node.next.title == key:
                return node.next
            node = node.next
        return node

    def __delitem__(self, key):
        if self.title == key:
            node = self
        else:
            node = self.__getitem__(key)
        node.prev.next = node.next
        node.prev.prev = node.prev.next

        if self.DEBUG:
            print
            print 'DELETING...', node.title, node.cargo
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
    _print('Linked List\n', path)


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


with Section('Arrays & Linked Lists'):
    DEBUG = True
    MAX_NODES = 10
    linked_list = build_list(MAX_NODES)
    print_nodes(linked_list)
    print 'Length of linked list:', len(linked_list)

    if DEBUG:
        print
        print 'Testing iteration'
        print
        for node in linked_list:
            print node

        del linked_list['node-1']
        del linked_list['node-4']
        del linked_list['node-2']
        del linked_list['node-6']
        del linked_list['tail']

        print
        print 'Testing iteration - post delete:'
        print
        for node in linked_list:
            print node

# Glossary practice

singleton = [1]
not_singleton = [1, 2]
