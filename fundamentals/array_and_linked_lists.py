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

from generic_helpers import section
from generic_helpers import _gibberish
from generic_helpers import _cmd_title


class Node:
    """A node represents a point in the linked list."""

    def __init__(self, title, cargo=None, next=None):
        self.title = title
        self.next = next
        self.cargo = cargo

    # These magic methods are not necessary;
    # just messing around with Python internals.

    def __del__(self):
        del self.cargo
        del self.next

    def __len__(self):
        count = 1  # Inclusive, head is 0
        node = self
        while node.next is not None:
            count += 1
            node = node.next
        return count

    def __add__(self, other):
        return 10 + len(other)

    def __mul__(self, other):
        return 10 * len(other)

    def length(self):
        return self.__len__()

    def remove(self, node):
        print ('Removing node `{}`, new node is `{}` which '
               'links to node `{}`').format(
                   self.next, node.next, node.next.next)
        self.next = node.next
        return node


def print_nodes(node):
    def _fmt(_node):
        return '[{}: {}]\n'.format(_node.title.upper(), _node.cargo)

    path = ''
    space_size = 4
    count = 0
    # Follows a node along it's next target, until next is None.
    _cmd_title('Printing Nodes')
    if node is not None:
        path += _fmt(node)
    while node is not None:
        if node.next is not None:
            pre = ' |{}'.format(space_size * '_')
            path += (count * '    ') + pre + _fmt(node.next)
            count += 1
        node = node.next
    print path
    print


def build_list(length):
    head = Node('head', cargo=_gibberish())
    node = head
    curr = 1  # head = 0
    while curr < length:
        if curr == length - 1:
            title = 'tail'
        else:
            title = 'node-{}'.format(curr)
        node.next = Node(title, cargo=_gibberish())
        node = node.next
        curr += 1
    return head


section('BEGIN - Arrays & Linked Lists')

# [head]--->[next]--->[next]--->[next]--->[tail]

head = Node(
    'head', cargo=_gibberish(), next=Node(
        'n1', cargo=_gibberish(), next=Node(
            'n2', cargo=_gibberish(), next=Node(
                'tail', cargo=_gibberish()))))

print_nodes(head)
print 'Length:', head.length()

l = build_list(40)
print_nodes(l)
print 'Length big list:', l.length()

# Glossary practice

singleton = [1]
not_singleton = [1, 2]

section('END - Arrays & Linked Lists')
