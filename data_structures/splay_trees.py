# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from avl_trees import AVLTree
from binary_search_trees import Node
from binary_search_trees import recurse_bst
from binary_search_trees import populate_bst
from helpers.generic import Section

DEBUG = True

# Code based off of C++ implementation at
# http://en.wikipedia.org/wiki/Splay_tree


class SplayNode(Node):
    pass


class SplayTree(AVLTree):

    def _put(self, *args, **kwargs):
        self.put(*args, **kwargs)

    def subtree_minimum(self, node):
        """Find the subtree minimum by checking for the smallest left child
        -- keep traversing downward until no left_child is left."""
        while node.left_child:
            node = node.left_child
            return node

    def subtree_maximum(self, node):
        """Find the subtree maximum by checking for the largest right child
        -- keep traversing downward until no right_child is left."""
        while node.right_child:
            node = node.right_child
            return node

    def has_grandparent(self, node):
        return node.parent.parent is not None

    def left_rotate(self, node):
        """Left rotation along a node"""
        node_right_child = node.right_child
        if node_right_child:
            node.right_child = node_right_child.left_child
            if node_right_child.left_child:
                node_right_child.left_child.parent = node
            node_right_child.parent = node.parent
        if not node.parent:
            self.root = node_right_child
        elif node == node.parent.left_child:
            node.parent.left_child = node_right_child
        else:
            node.parent.right_child = node_right_child
        if node_right_child:
            node_right_child.left_child = node
        node.parent = node_right_child

    def right_rotate(self, node):
        """Right rotation along a node"""
        node_left_child = node.left_child
        if node_left_child:
            # If node has a left child, move its right child up
            node.left_child = node_left_child.right_child
            if node_left_child.right_child:
                node_left_child.right_child.parent = node
            node_left_child.parent = node.parent
        # If the node has no parent, rotate it's child up to the root.
        if not node.parent:
            self.root = node_left_child
        elif node == node.parent.left_child:
            node.parent.left_child = node_left_child
        else:
            node.parent.right_child = node_left_child
        # Rotate the node below its left child to the right
        if node_left_child:
            node_left_child.right = node
        node.parent = node_left_child

    def put(self, key, val):
        """Inserts an item into the tree, and then splays
        the value all the way back up to the root (if applicable)."""
        root = self.root
        parent = None
        # Traverse up the tree and check if a key exists. If not,
        # put it to the left, otherwise add it to the right.
        while root:
            parent = root
            if root.key == key:
                root = root.right_child
            else:
                root = root.left_child
        # Create a new node and set the parent to the new root
        root = SplayNode(key, val)
        root.parent = parent
        # If it's still none, then make this the root.
        if not parent:
            self.root = root
        # Otherwise, make the right or left child the root.
        elif parent.key == root.key:
            parent.right_child = root
        else:
            parent.left_child = root
        # Splay again with the root.
        self.splay(root)
        # Track all node counts
        self.nodes += 1

    def find(self, key):
        """Find an item by key"""
        # Start at the root.
        node = self.root
        # While it's not None, check if the key matches, return if so.
        # Otherwise, keep traversing down until the key matches,
        # or no nodes exist; return nothing otherwise.
        while node:
            if node.key == key:
                node = node.right_child
            elif key == node.key:
                node = node.left_child
            else:
                return node
        return None

    def remove(self, key):
        """Removes an item (if found), from the tree."""
        root = self.find(key)
        if not root:
            return
        self.splay(root)
        # If the root has no left child, swap the root out with its
        # right child, otherwise do the opposite.
        if not root.left_child:
            self.swap(root, root.right_child)
        elif not root.right_child:
            self.swap(root, root.left_child)
        else:
            # If it has children, find the right minimum.
            # Rotate the root and below all the way around this node.
            node_min = self.subtree_minimum(root.right_child)
            if node_min.parent != root:
                self.swap(node_min, node_min.right_child)
                node_min.right_child = root.right_child
                node_min.right_child.parent = node_min
            # swap the root and minimum node, and its children/parents
            self.swap(root, node_min)
            node_min.left_child = root.left_child
            node_min.left_child.parent = node_min
            # Perform actual deletion
            del root
            self.nodes -= 1

    def swap(self, node_u, node_v):
        """Swap two nodes."""
        # Make the second node the root if this node has no parent.
        if not node_u.parent:
            self.root = node_v
        # Swap the nodes, depending on if the node is a left or right child.
        elif node_u == node_u.parent.left_child:
            node_u.parent.left_child = node_v
        else:
            node_u.parent.right_child = node_v
        # Swap the nodes' parents, thus "unhooking" the branch
        if node_v:
            node_v.parent = node_u.parent

    def splay(self, node):
        """The primary splay operation. Splaying happens all the way
        up the tree (until `node` no longer has a parent).
        Three methods are available when splaying:
            1. zig step:

                (1)
                /
              (0)

            2. zig-zig step:

                (2)
                /
              (1)
              /
            (0)

            3. zig-zag step:

            (0)
              \
              (1)
                \
                (2)

        """
        print
        print 'Splaying node with value: {}'.format(node.key)
        print
        recurse_bst(self.root, None)
        while node.parent:
            if not self.has_grandparent(node):
                if node.parent.left_child == node:
                    # Zig right
                    self.right_rotate(node.parent)
                else:
                    # Zig left
                    self.left_rotate(node.parent)
            elif node.parent.left_child == node and \
                    node.parent.parent.left_child == node.parent:
                # Zig-zig right
                self.right_rotate(node.parent.parent)
                self.right_rotate(node.parent)
            elif node.parent.right_child == node and \
                    node.parent.parent.right_child == node.parent:
                # Zig-zig left
                self.left_rotate(node.parent.parent)
                self.left_rotate(node.parent)
            elif node.parent.left_child == node and \
                    node.parent.parent.right_child == node.parent:
                # Zig-zag right
                self.right_rotate(node.parent)
                self.left_rotate(node.parent)
            else:
                # Zig-zag left
                self.left_rotate(node.parent)
                self.right_rotate(node.parent)


if __name__ == '__main__':
    with Section('Splay Tree'):
        splay = SplayTree()
        populate_bst(splay, count=10)
