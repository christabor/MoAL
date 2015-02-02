# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))


from generic_helpers import Section
from generic_helpers import divide_groups
from generic_helpers import random_number_set
from quick_sort import quick_sort
from pprint import pprint as ppr
from Queue import Queue
from threading import Lock
from threading import Thread


SORT_LOCK = Lock()


class ThreadSort:
    """An experiment to divide a list of items up into sub-groups
    and then sort them individually on different threads.
    Doesn't really perform better than the original algorithm,
    though it could be useful for processing individual lists separately."""

    def __init__(self, sorting_func, threads=2):
        self.threads = threads
        self.sorting_func = sorting_func
        self.sorting_queue = Queue()
        self.sorted_items = []

    def _disperse(self):
        for _ in range(self.threads):
            t = Thread(target=self._worker, kwargs={
                'sorted_items': self.sorted_items})
            t.daemon = True
            t.start()
        return self

    def _worker(self, sorted_items=None):
        while True:
            items = self.sorting_queue.get()
            self.sorted_items += self.sorting_func(items)
            self.sorting_queue.task_done()

    def _enqueue(self, items):
        # Get the number of thread groups to run based on length and threads.
        groups = divide_groups(items, divisions=self.threads)
        # For each sub group, sort on a separate thread.
        for group in groups:
            self.sorting_queue.put(group)
        return self

    def run(self, items):
        # Make sure thread number is never greater than the number of items.
        num_items = len(items)
        while self.threads > num_items:
            self.threads -= 1
        if num_items < 2:
            return items
        # Prevent passing in div by zero errors.
        if self.threads == 0:
            self.threads = 1
        self._disperse()._enqueue(items)
        # Block until complete.
        self.sorting_queue.join()
        # Perform the second sort on already sorted sublists.
        # print self.sorting_func(self.sorted_items)
        return self.sorting_func(self.sorted_items)


with Section('Threaded Sorts'):
    threaded_quicksort = ThreadSort(quick_sort, threads=4)

    rand = random_number_set(max_range=20)
    res = threaded_quicksort.run(rand)
    print 'Is valid?', res == sorted(rand)
    ppr(res)
