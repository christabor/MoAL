# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import cmd_title
from Queue import Queue
from threading import Lock
from threading import Thread
import time

STREAM_LOCK = Lock()
DEBUG = True if __name__ == '__main__' else False


class Stream(Queue):

    def __init__(self):
        self.items = []
        self.total_read = 0

    def add(self, item):
        self.__setitem__(str(item))

    def not_empty(self):
        """Report if the stream still has items - this is nonsensical in some
        cases since a stream by definition is potentially infinite."""
        return len(self.items) > 0

    def read(self):
        try:
            end = self.items.pop()
        except IndexError:
            cmd_title('All items have been read.')
            return None
        if DEBUG:
            print('Reading new item from stream... {}\n'.format(end))
            print('[CURRENT STREAM] {}\n'.format(' -- '.join(self.items)))
        self.total_read += 1
        return end

    def __setitem__(self, item):
        if DEBUG:
            print('Adding new item to stream... {}\n'.format(item))
        self.items.append(item)


def process_with_lock(func):
    STREAM_LOCK.acquire()
    func()
    STREAM_LOCK.release()


if DEBUG:
    with Section('Stream Abstract Data Type'):
        # Prevent threads from running forever, since this is just a simulation.
        MAX_ITERATIONS = 99
        ADD_INTERVAL = 0.1
        # Much longer than add, for effect (though in a real system,
        # it would likely be a fraction as well, to prevent unnecessary
        # reads to the system, whether it be distributed or local.)
        READ_INTERVAL = 0.5
        # In later work, perhaps in a new module, it would be interesting
        # and useful to implement an exponential 'back-off' OR increase,
        # to "tighten" or "loosen" the flow of data, so `read_interval`
        # and `write_interval` might adjust as the number of items changes.
        data_stream = Stream()
        n_val = 0

        def stream_write():
            cmd_title('Thread starting in WRITE mode', newlines=False)
            global n_val
            while n_val < MAX_ITERATIONS:
                time.sleep(ADD_INTERVAL)
                data_stream.add(n_val)
                n_val += 1

        def stream_read():
            cmd_title('Thread starting in READ mode', newlines=False)
            # Force an initial warm up so it doesn't terminate early.
            time.sleep(0.2)
            # Here (in the while loop), we use a different termination strategy
            # so we can simulate draining the stream until all items are clear.
            while data_stream.not_empty():
                time.sleep(READ_INTERVAL)
                data_stream.read()

        read_thread = Thread(target=stream_read)
        write_thread = Thread(target=stream_write)
        read_thread.daemon = True
        write_thread.daemon = True
        read_thread.start()
        write_thread.start()
        # Simulate a running process that continually
        # reads and writes to the stream.
        process_with_lock(stream_write)
        process_with_lock(stream_read)
