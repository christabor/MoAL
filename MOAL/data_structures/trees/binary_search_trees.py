# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


from random import randrange
from MOAL.helpers.text import gibberish
from MOAL.helpers.display import Section


class BinarySearchTree:
    """BST Code sample originally from interactivepython.org
        /runestone/static/pythonds/Trees/bst.html#lst-bst1,
        with some modifications.
    """

    def __init__(self):
        # Default to no "top/root" root element
        self.root = None
        # This tree has no nodes by default
        self.nodes = 0
        # Keep track of leaves and nodes for fun/practice
        self.leaves = self.nodes - 1 if self.nodes > 0 else 0

    def __len__(self):
        # Allow native python len() on the object
        return self.nodes

    def __iter__(self):
        # Allow native python iterables
        if self.root is not None:
            return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)

    def length(self):
        return self.nodes

    def put(self, key, val):
        # This public method uses _put but always with self.root
        # as the current_node

        # If this is the root, then do some extra checks
        # to make sure the ordering is correct...
        if self.root:
            self._put(key, val, self.root)
        else:
            # ...make this the new root otherwise
            self.root = Node(key, val)
        self.nodes += 1

    def _put(self, key, val, current_node):
        # If the given key is greater than the given nodes key,
        # put it on right of that node, otherwise put it on the left.
        if key < current_node.key:
            # If the child node already has a node, then
            # start again with this new child node as the current_node,
            # recursively working all the way down until the other condition
            # is true (no children exist for this node)
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                # Finally, once the recursion above has eliminated all
                # child nodes from our selection, we create a new
                # node for this position, and make this node its parent.
                current_node.left_child = Node(key, val, parent=current_node)
        else:
            # Same thing, but for the right side.
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = Node(key, val, parent=current_node)

    def get(self, key):
        return self._get(key, self.root) if self.root else None

    def _get(self, key, current_node):
        # Return nothing if no node was given.
        if not current_node:
            return None
        # If the keys match, we've found our node.
        elif current_node.key == key:
            return current_node
        # If the key is less than the current node, return its left child.
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        # If the key is greater than the current node, return its right child.
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        if self.nodes > 1:
            # If nodes below the root exist,
            # delete the root node or its leaf (if any).
            node = self._get(key, self.root)
            if node is not None:
                self.remove(node)
                self.nodes = self.nodes - 1
            else:
                raise KeyError('No such key.')
        # If the only node that exists is the root, delete it.
        elif self.nodes == 1 and self.root.key == key:
            self.root = None
            self.nodes = self.nodes - 1
        else:
            raise KeyError('No such key')

    def find_min(self):
        current = self
        # Keep working down the left side until the current
        # node no longer has a left child, which is accomplished
        # by continually re-assigning the left child.
        # e.g:
        #                     O
        # current:           /
        # new current:      /
        # new new current: / <-- target
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            # If this node is a leaf, prune either the left or right node
            # from its parent, depending on which side this node is on.
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    # If this node has AND is a left child,
                    # then the parents left child becomes this nodes'
                    # left child node, thus splicing it out of the group.
                    self.parent.left_child = self.left_child
                else:
                    # Same rule, but replace the right side instead.
                    self.parent.right_child = self.right_child
                # Once spliced out, we also need to update the other
                # reference for each child node to point to the
                # current nodes parent, instead of this node.
                # That way, no dead references exist.
                self.left_child.parent = self.parent
            else:
                # If the node is a left child, but has no left children
                # of its own (instead having only right children),
                # then replace the parents left child with this right child
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    # Otherwise, swap the behavior -- replace the
                    # parents right child with this right child.
                    self.parent.right_child = self.right_child
                # Update these references as well, but for the opposite side.
                self.right_child.parent = self.parent

    def find_successor(self):
        # There is no successor if the node has
        # no right child and has no parent.
        successor = None
        # If this node has a right child, the successor is somewhere
        # to the right -- specifically the node with the
        # minimum value for the right subtree.
        if self.has_right_child():
            successor = self.right_child.find_min()
        else:
            # If it has no right child and it has a parent.
            if self.parent:
                # If it has a parent and is to the left of it, then
                # the parent is the successor.
                if self.is_left_child():
                    successor = self.parent
                else:
                    # Otherwise, it has a parent and is to the right of it.
                    # In that case, remove this node from the parent...
                    self.parent.right_child = None
                    # ...and keep searching the parent.
                    successor = self.parent.find_successor()
                    # Once the successor is found, re-assign the current node
                    # to be the parents' right child.
                    self.parent.right_child = self
        return successor

    def _swap_current(self, current_node, side):
        if side == 'left':
            current_node.swap_node(
                current_node.left_child.key,
                current_node.left_child.data,
                current_node.left_child.left_child,
                current_node.left_child.right_child)
        else:
            current_node.swap_node(
                current_node.right_child.key,
                current_node.right_child.data,
                current_node.right_child.left_child,
                current_node.right_child.right_child)

    def remove(self, current_node):
        # If the current node is a leaf, check if it's
        # the left or the right node of the parent, and remove it accordingly.
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            # If it has left and right children,
            # find the successor from either branch,
            # and then re-assign its values
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.data = successor.data
        else:
            if current_node.has_left_child():
                # If the current node has and IS the left child,
                # promote it to up to the replace its parent.
                # Also promote the child (left or right) node up as well.
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                # If its neither the left or child, then make a new node
                # with the current_node grandchildren
                else:
                    self._swap_current(current_node, 'left')
            # Deal with non leaf nodes
            else:
                # Do the same, but for the right side instead.
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    self._swap_current(current_node, 'right')


class Node:

    def __init__(self, key, val, left=None, right=None, parent=None):
        # Assign locally for reference by the entire object.
        self.key = key
        self.data = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

    def __iter__(self):
        # This method seemingly iterates over one node only, but since
        # it is overriding the `for **in** x` behavior, it is called for each
        # node, which makes it recursive, thus covering all nodes.
        if self:
            # Yield left nodes if they exist
            if self.has_left_child():
                for node in self.left_child:
                    yield node
            yield self.key
            # Yield right nodes if they exist.
            if self.has_right_child():
                for node in self.right_child:
                    yield node

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def is_left_child(self):
        # See if it has a parent, and if the parent's
        # left child is this node.
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        # See if it has a parent, and if the parent's
        # right child is this node.
        return self.parent and self.parent.right_child == self

    def is_root(self):
        # See if it's the top node. By default, root is set to None.
        return self.parent is None

    def is_leaf(self):
        # See if this is the leaf (it has no child nodes below it)
        return self.right_child is None and self.left_child is None

    def has_any_children(self):
        # See if it has any nodes below it - left or right.
        return self.right_child is not None or self.left_child is not None

    def has_both_children(self):
        # See if it has both nodes below it - left and right.
        return self.right_child is not None and self.left_child is not None

    def swap_node(self, key, value, left_child, right_child):
        self.key = key
        self.data = value
        # Re-assign child nodes.
        self.left_child = left_child
        self.right_child = right_child
        # Check that the new nodes actually exist, and
        # make this node the new parent.
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


# Testing/Experimenting
def recurse_bst(node, lastkey):
    char = None
    if node is None:
        return
    offset = node.key / 2
    if lastkey is None:
        char = '|'
    elif lastkey > node.key:
        char = ' /'
    else:
        char = '\\'

    if lastkey is not None:
        diff = abs(lastkey - node.key) / 2
        connector = ('.' * diff)
        if diff > 2:
            if lastkey < node.key:
                print('{} {}'.format(''.ljust(offset - diff), connector))
            else:
                print('{} {}'.format(
                    ''.ljust(offset - (diff / 8) + 2), connector))

    print('{} {}'.format(''.ljust(offset), char))
    print('{} {}'.format(''.ljust(offset), node.key))

    if node.left_child is not None:
        recurse_bst(node.left_child, node.key)
    if node.right_child is not None:
        recurse_bst(node.right_child, node.key)


def populate_bst(bst, count=1):
    for _ in range(count):
        bst.put(randrange(1, 100), gibberish())


if __name__ == '__main__':
    with Section('Binary Search Trees'):
        bst = BinarySearchTree()
        populate_bst(bst, count=5)
        print('\n')
        recurse_bst(bst.root, None)
        print('\n')

        # Basic test assertions
        bst.put(100, 'testing')
        assert 100 in bst
        del bst[100]
        assert 100 not in bst
        bst.put(100, 'testing')
        bst.put(101, 'testing')
        assert 101 in bst
        f = bst.get(100)
        assert f.has_right_child()
        assert not f.has_left_child()
