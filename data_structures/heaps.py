# -*- coding: utf-8 -*-

# Mostly taken from:
# http://interactivepython.org/runestone/static/pythonds/Trees/heap.html

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from random import randrange as rr
import data_structures.binary_search_trees as bst


class BinHeap(bst.BinarySearchTree):

    def __init__(self, new_list):
        print 'Original list:', new_list
        i = len(new_list)
        self.size = len(new_list)
        # Shallow copy of the list handed over, plus the root node `[0]`
        # added on to the beginning.
        self.heap_list = [0] + new_list[:]
        # Create the list, then sort it all the way down
        # based on the heap property
        while i > 0:
            self.swap_down(i)
            i -= 1
        print 'New list:', self.heap_list

    def insert(self, item):
        # This is just a normal insert, except it re-balances
        # the heap after words.
        self.heap_list.append(item)
        self.size += 1
        # Use size as the key indicator
        self.swap_up(self.size)

    def del_min(self):
        # Find the first (non root) node - 0 is root.
        node = self.heap_list[1]
        # Assign second key to the last element
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        # Pop off the last item
        self.heap_list.pop()
        # Re-calculate after it has been removed
        self.swap_down(1)
        return node

    def min_child_index(self, i):
        # Get the current index and determine if it's past the end or not
        # -- the furthest in the list indices represents the smallest.
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            # If it's not the end, see if its key is smaller than the next one
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                # If not, this one is the smallest, so return it.
                return i * 2 + 1

    def swap_up(self, i):
        print 'Swapping up index: {}'.format(i)
        while i // 2 > 0:
            # Run while current heap node is less than node // 2
            # (which is the node before it)
            if self.heap_list[i] < self.heap_list[i // 2]:
                # Store the tmp value, and then swap them and restore.
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            # Keep subdividing i
            i = i // 2

    def swap_down(self, i):
        print 'Swapping down index: {}'.format(i)
        # Like swap up, but moves down the list.
        while (i * 2) <= self.size:
            # Find the minimum child for the subtree
            min_child_index = self.min_child_index(i)
            if self.heap_list[i] > self.heap_list[min_child_index]:
                # Store a temp, then swap and restore.
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child_index]
                self.heap_list[min_child_index] = tmp
            i = min_child_index


# Example implementations

class PriorityQueue(BinHeap, object):

    def __init__(self, *args, **kwargs):
        super(PriorityQueue, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    with Section('Binary Heaps'):
        my_heap = BinHeap([rr(1, 100) for _ in range(30)])
        print my_heap

    with Section('Priority Queue'):
        pq = PriorityQueue([rr(1, 100) for _ in range(30)])
        print
        for _ in range(10):
            pq.insert(rr(1, 100))
