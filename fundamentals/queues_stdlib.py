# Concepts/learning from:
# http://inventwithpython.com/blog/2013/04/22/multithreaded-python-tutorial-with-threadworms/
from Queue import Queue
import threading

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# from random import choice
from generic_helpers import _gibberish
from generic_helpers import section


section('BEGIN - Python stdlib Queue and multi-threading examples')

COUNT_LOCK = threading.Lock()
TOTAL = 1

class CountThread(threading.Thread):

    def start(self, name):
        # Allow adding a name when start is called,
        # but still defer to superclass method
        self.name = name
        super(CountThread, self).start()

    def run(self):
        # Make TOTAL a global variable, outside the scope of this
        # function/class to demonstrate the thread updates
        global TOTAL
        for i in range(1000):
            # Must acquire and then release lock after every operation,
            # otherwise the global mutable state will be overwritten for each
            # thread that runs, resetting the value, which is significantly
            # lower than the correct TOTAL.
            COUNT_LOCK.acquire()
            TOTAL += 1
            COUNT_LOCK.release()
        print 'Total processed by {}: {}:'.format(self.name, TOTAL)


counter_one = CountThread()
counter_two = CountThread()
counter_three = CountThread()
counter_one.start('one')
counter_two.start('two')
counter_three.start('three')

print '** these dividers will not work right since the threads are ND and the end of this line is not guaranteed to come before the end of the thread processes! **'
section('END - Python stdlib Queue and multi-threading examples')

# Some basic code taken from https://docs.python.org/2/library/queue.html


class Worker:

    def __init__(self, queue, num_threads=2):
        self.NUM_THREADS = num_threads
        self.queue = queue

    def do_work(self, item):
        print 'Working on item... {}\n'.format(item)

    def worker(self):
        while True:
            item = self.queue.get()
            self.do_work(item)
            self.queue.task_done()

    def process_all(self):
        print 'Starting all process threads...'
        for _ in range(self.NUM_THREADS):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()


class Producer:

    def __init__(self):
        self.items = []

    def __iter__(self):
        for record in self.items:
            yield record

    def add(self):
        self.items.append(self.make())

    def make(self):
        return _gibberish()

section('BEGIN - Python stdlib Queue and multi-threading examples 2')

work_queue = Queue()
bot = Worker(work_queue)
producer = Producer()

for _ in range(10):
    producer.add()

for record in producer:
    print 'Putting record {} into queue.'.format(record)
    work_queue.put(record)

bot.process_all()

# Block until done
work_queue.join()

print '** these dividers will not work right since the threads are ND and the end of this line is not guaranteed to come before the end of the thread processes! **'
section('END - Python stdlib Queue and multi-threading examples 2')
