# Mostly taken from:
# interactivepython.org/runestone/
# static/pythonds/BasicDS/ImplementingaStackinPython.html

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from random import randrange
from generic_helpers import _gibberish
from generic_helpers import section
from pprint import pprint as ppr


class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def tail(self):
        return self.items[0]

    def head(self):
        return self.peek()

    def view(self):
        return self.items


STACK_COUNT = 10

section('BEGIN - Stacks')
stack = Stack()
print
print 'First in push'
print
for _ in range(STACK_COUNT):
    stack.push('{} ... [ {} ]'.format(_, _gibberish()))
    print stack.head()

print
print stack.size(), stack.view()
print
print 'First out pop'
print
for _ in range(STACK_COUNT):
    print stack.pop()

print
print stack.size(), stack.view()
section('END - Stacks')


# Example 'real world usage'

class Logger(Stack):

    def __init__(self, *args, **kwargs):
        self.items = []

    def add_message(self, message, priority=0):
        self.push({
            'priority': priority,
            'message': message
        })

    def get_by_priority(self, priority):
        matches = []
        for item in self.items:
            if item['priority'] == priority:
                matches.append(item)
        return ppr(matches)

    def view_messages(self):
        return ppr(super(Logger, self).view())

    def get_last_message(self):
        return self.pop()

    def get_first_message(self):
        return self.tail()

section('BEGIN - Logger')
logger = Logger()
for _ in range(STACK_COUNT):
    logger.add_message(_gibberish(length=10), priority=randrange(0, 10))
print logger.view_messages()
print logger.get_by_priority(4)
print logger.get_last_message()
print logger.get_first_message()
section('END - Logger')

# Example 'real world usage' with extensions, OOP


class WebLogger(Logger):

    def add_message(self, message, priority=0):
        return super(WebLogger, self).add_message(
            '[WEBLOG] - ' + message, priority=priority)


class NetworkLogger(Logger):

    def add_message(self, message, priority=0):
        return super(NetworkLogger, self).add_message(
            '[NETWORK] - ' + message, priority=priority)

section('BEGIN - Loggers (continued)')
wl = WebLogger()
nl = NetworkLogger()

for _ in range(STACK_COUNT):
    wl.add_message(_gibberish(length=10), priority=randrange(0, 10))

for _ in range(STACK_COUNT):
    nl.add_message(_gibberish(length=10), priority=randrange(0, 10))

print wl.view_messages()
print nl.view_messages()

section('END - Loggers (continued)')
