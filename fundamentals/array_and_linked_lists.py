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


class Node:
    """A node represents a point in the linked list."""

    def __init__(self, pk, cargo=None, next=None):
        self.pk = pk
        self.next = next
        self.cargo = cargo

    """These magic methods are not necessary
    -- just messing around with Python internals."""

    def __del__(self):
        del self.cargo
        del self.next

    def __len__(self):
        return self.cargo

    def __add__(self, other):
        return 10 + len(other)

    def __mul__(self, other):
        return 10 * len(other)

    def remove(self, node):
        print ('Removing node `{}`, new node is `{}` which '
               'links to node `{}`').format(self.pk, node.pk, node.next.pk)
        self.next = node.next
        return node


class List():
    """Implements a pseudo-list by using a collection of nodes."""

    def __init__(self, node):
        # Kind of pointless since we're just using a real list
        # behind-the-scenes, but it will suffice for demonstration.
        self.nodes = [node]

    def __len__(self):
        return len(self.nodes)

    def add(self, node):
        self.nodes += [node]

    def view(self):
        print 'NODES: ', self.nodes


section('BEGIN - Arrays & Linked Lists')
a_node1 = Node(1, cargo=100, next=10)
a_node2 = Node(2, cargo=10, next=20)
print a_node1 + a_node2, a_node1 * a_node2

node3 = Node(3, cargo=30)
node2 = Node(2, next=node3, cargo=20)
node1 = Node(1, next=node2, cargo=10)
# ...and so on...

l = List(node1)
l.add(node2)
l.add(node3)

print '{} is of length: {}'.format(l, len(l))
print l.view()


def print_nodes(node):
    space_size = 5
    path = ''
    """Follows a node along it's next target, until next is None."""
    print '==== Showing nodes...'
    while node is not None:
        path += ' {}> [{}]'.format((space_size * '-'), node.next)
        node = node.next
    print path
    print '===='

print_nodes(node1)

print node1.remove(node2)

"""Glossary practice"""

singleton = [1]
not_singleton = [1, 2]
node = Node(9999)
linked_list = List(node)
cargo = node.cargo
section('END - Arrays & Linked Lists')
