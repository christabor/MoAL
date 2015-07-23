# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import print_simple
from MOAL.helpers.display import Section
from MOAL.data_structures.abstract.queues import Queue


DEBUG = True if __name__ == '__main__' else False


class PriorityQueue(Queue):

    def __init__(self, *args, **kwargs):
        super(PriorityQueue, self).__init__(*args, **kwargs)
        # Keep a max level to reference from.
        self.max_priority = 0

    def __str__(self):
        print_simple('<PriorityQueue>', self.items)
        return ''

    def enqueue(self, item, priority=0):
        item = {'priority': priority, 'data': item}
        # Update max if it has increased.
        if priority > self.max_priority:
            self.max_priority = priority
        return super(PriorityQueue, self).enqueue(item)

    def pull_highest_priority_element(self):
        return self.get_priority(self.max_priority)

    def get_priority(self, level):
        """Naive implementation - does not consider duplicate priority levels"""
        for k, el in enumerate(self.items):
            if el['priority'] == level:
                return self.items.pop(k)
        return None


if DEBUG:
    with Section('Priority Queues'):
        pq = PriorityQueue()
        pq.enqueue('pq-item-0', priority=0)
        pq.enqueue('pq-item-4', priority=4)
        pq.enqueue('pq-item-5', priority=5)
        pq.enqueue('pq-item-3', priority=3)
        pq.enqueue('pq-item-1', priority=1)
        pq.enqueue('pq-item-2', priority=2)
        print(pq)
        firstlen = len(pq)

        item = pq.get_priority(4)
        assert item['data'] == 'pq-item-4'

        item = pq.get_priority(0)
        assert item['data'] == 'pq-item-0'

        item = pq.get_priority(10)
        assert item is None

        print(pq)
        assert len(pq) < firstlen
