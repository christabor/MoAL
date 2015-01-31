# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from random import choice
from generic_helpers import _gibberish
from generic_helpers import section
from stack import Stack


class Queue(Stack):

    def __init__(self, *args, **kwargs):
        super(Queue, self).__init__(*args, **kwargs)

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return super(Queue, self).pop()

    def move_to_end(self):
        self.enqueue(self.dequeue())

    def out_of_range(self):
        return len(self.items) - 1 < self.num


class Dequeue(Queue):

    """Represents a 'double ended' queue -- a queue that can use either
    direction as the head/tail, but works the same way."""

    def __init__(self, direction):
        self.direction = direction
        super(Dequeue, self).__init__()

    def enqueue(self, item):
        if self.direction == 'backwards':
            self.items.insert(len(self.items) - 1, item)
        else:
            super(Dequeue, self).enqueue(item)

    def dequeue(self):
        if self.direction == 'backwards':
            self.items.remove()
        else:
            super(Dequeue, self).enqueue()


section('BEGIN - Queues')

q = Queue()
for _ in range(5):
    print 'en-queuing new item...'
    q.enqueue(_gibberish())

section('BEGIN - Double ended queue')

dq = Dequeue('backwards')
for _ in range(5):
    print 'en-queuing (dequeue) new item...'
    dq.enqueue(_gibberish())

section('BEGIN - Queue rotation example')


class HotPotatoSimulator(Queue):

    def __init__(self, names, num):
        super(HotPotatoSimulator, self).__init__()
        self.num = num
        self.items = names

    def adjust_position(self):
        print 'Out of range... adjusting position to a valid index.'
        # If `self.num` is greater than the length of the list,
        # keep adjusting until it's in range.
        while self.out_of_range():
            self.num -= 1
            self.adjust_position()

    def move(self):
        if self.out_of_range():
            print 'No items in the queue to move!'
            return self.adjust_position()
        person = self.items[self.num]
        print 'Moving around circle {} times to: {}'.format(self.num, person)
        print self.items
        self.move_to_end()

hps = HotPotatoSimulator(
    ['Tuvok', 'Neelix', 'Kim', 'Paris', 'Seven', 'Chakotay'], 20)

for _ in range(7):
    hps.move()


section('BEGIN - Printer queue example')


class PrinterQueue(Queue):

    def add_job(self, name, doc):
        self.push({'name': name, 'doc': doc})
        print 'Adding {} to queue for printing...'.format(name)

    def print_job(self):
        print 'Printing... {}'.format(self.head()['name'])

pq = PrinterQueue()
for _ in range(10):
    pq.add_job('My_doc_{}.{}'.format(
        _gibberish(), choice(
            ['doc', 'docx', 'rtf', 'pdf', 'jpg', '.png'])),
        '<DOC CONTENTS...>')

for _ in range(10):
    pq.print_job()

section('END - All queue examples')
