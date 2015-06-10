# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class InvalidBufferLength(Exception):
    pass


class CircularBuffer(list):

    def __init__(self, items, **kwargs):
        # Testing enforcement of maximum ring size
        self.MAX_SIZE = 8
        # Keep a "pointer" to the active index; it starts at 0.
        self.pointer = 0
        if not isinstance(items, list):
            raise TypeError
        if len(items) > self.MAX_SIZE:
            raise InvalidBufferLength(
                'Number of items cannot exceed {}'.format(self.MAX_SIZE))
        super(CircularBuffer, self).__init__(items, **kwargs)

    def __str__(self):
        indices = map(str, range(len(self)))
        chars = map(str, self)
        print('Current pointer: {}\n{}'.format(
            self.pointer, ' ' + '   '.join(indices)))
        return '[{}]'.format('] ['.join(chars))

    def __delitem__(self, key):
        # Delitem becomes a no-op here because we just overwrite items instead.
        pass

    def __getitem__(self, key):
        return super(CircularBuffer, self).__getitem__(key)

    def __setitem__(self, index, value):
        # If the pointer is at the end, append the value at the beginning.
        old = self.pointer
        if self.pointer >= self.MAX_SIZE:
            # Reset pointer position to the beginning, **before** appending.
            self.pointer = 0
            super(CircularBuffer, self).__setitem__(self.pointer, value)
        else:
            # Set the given value
            super(CircularBuffer, self).__setitem__(index, value)

        # Update pointer **after**
        self.pointer += 1
        print('  POINTER: {} => {}'.format(old, self.pointer))

    def append(self, value):
        return self.__setitem__(self.pointer, value)


if DEBUG:
    with Section('Array - Circular Buffer'):
        # Populate a full buffer
        circbuff = CircularBuffer(range(8))
        print(circbuff)

        # Start overwriting values
        circbuff.append('A')
        circbuff.append('B')
        circbuff.append('C')
        circbuff.append('D')
        circbuff.append('E')
        circbuff.append('0')
        circbuff.append('10')
        print(circbuff)

        # Test that the indices have been overwritten properly.
        assert circbuff[0] == 'A'
        assert circbuff[1] == 'B'
        assert circbuff[2] == 'C'
        assert circbuff[3] == 'D'
        assert circbuff[4] == 'E'

        # Add some more to check...
        circbuff.append('Z')
        circbuff.append('X')
        circbuff.append('Y')

        # Check that it wraps around properly (again).
        assert circbuff[7] == 'Z'
        assert circbuff[0] == 'X'
        assert circbuff[1] == 'Y'

        print(circbuff)
