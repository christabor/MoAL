# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_h3
from helpers.display import print_h4
from time import sleep
from math import factorial

DEBUG = True if __name__ == '__main__' else False


class BaseDataType(object):
    """The irony here is that these data types take up significantly
    more actual memory as a class representation in a bytecode interpreted
    language. The classing is merely for intuitive understanding and
    representing the hierarchy/operations."""

    @staticmethod
    def _alter(old_bit, new_bit, value):
        """An interesting visualization of flipping bits --
        not very robust; primarily meant as a basic learning exercise
        -- see other relevant modules for more specific implementations."""
        if not isinstance(value, str):
            raise TypeError('Requires a string version to prevent coercion.')
        curr_index = len(value) - 1
        # Convert the binary values to a list for operating on
        new = list(value)
        # Store a copy string representation for visual comparisons
        old = ''.join(new)
        # Keep moving right until we get to the next on/off bit
        # (depending on whether we're incrementing or decrementing)
        while new[curr_index] == old_bit:
            curr_index -= 1
            new[curr_index + 1] = new_bit
        try:
            new[curr_index] = old_bit
        except IndexError:
            pass
        new = ''.join(new)
        value = new
        return old, new

    @staticmethod
    def decrement(value):
        old, new = BaseDataType._alter('0', '1', value)
        if DEBUG:
            print('\ndecrement: \n{}\n{}'.format(old, new))
        return new

    @staticmethod
    def increment(value):
        old, new = BaseDataType._alter('1', '0', value)
        if DEBUG:
            print('\nincrement: \n{}\n{}'.format(old, new))
        return new

    @staticmethod
    def add(binval, amount):
        for n in range(amount):
            binval = BaseDataType.increment(binval)
        return binval

    @staticmethod
    def subtract(binval, amount):
        for n in range(amount):
            binval = BaseDataType.decrement(binval)
        return binval

    @staticmethod
    def multiply(binval, amount):
        # Just defer to increment,
        # e.g. 10 * 2 = 20, |10 - 20| = 10 ... inc. 10
        product = int(binval) * amount
        diff = abs(int(binval) - product)
        for n in range(diff):
            binval = BaseDataType.increment(binval)
        return binval

    @staticmethod
    def divide(binval, amount):
        # Just defer to decrement,
        # e.g. 10 / 2 = 5, 10 - 5 = 5 ... dec. 5
        quotient = int(binval) // amount
        diff = abs(int(binval) - quotient)
        for n in range(diff):
            binval = BaseDataType.decrement(binval)
        return binval

    def get_least_significant(self):
        return self.value[-1]

    def get_most_significant(self):
        return self.value[0]

    def get_max_binvals(self):
        if not hasattr(self, 'value'):
            raise TypeError
        else:
            val = len(self.value)
            return 2 if val == 1 else factorial(val)

    def __str__(self):
        if self.value:
            return '[{}]'.format(self.value)
        else:
            return ''


class Bit(BaseDataType):

    def __str__(self):
        return '[{}]'.format('] ['.join(self.value))

    def __init__(self, value):
        self.bits = []
        self.value = value


class Nibble(Bit):

    def __init__(self, value):
        self.length = 4
        super(Nibble, self).__init__(value)
        for char in value:
            self.bits.append(Bit(char))


class Byte(Nibble):

    """Also sometimes referred to as an `Octet`"""

    def __init__(self, value):
        self.length = 8
        super(Byte, self).__init__(value)


class Halfword(Nibble):

    def __init__(self, value):
        self.length = 16
        super(Halfword, self).__init__(value)


class Word(Nibble):

    def __init__(self, value):
        self.length = 32
        super(Word, self).__init__(value)


def update_animation(steps, func, instance):
    for _ in range(steps):
        sleep(0.05)
        instance.value = func(instance.value)


bin_inc = BaseDataType.increment
bin_dec = BaseDataType.decrement


if __name__ == '__main__':
    with Section('Computer organization - Data types'):
        print_h4('Bit', desc='The simplest unit of information.')
        bit = Bit('0')
        assert bit.get_max_binvals() == 2

        print_h3('Nibble', desc='4 bits = 1/2 byte.')
        nibble = Nibble('0000')
        print(nibble)
        assert nibble.get_max_binvals() == 24

        print_h3('Byte', desc='8 bits = one byte.')
        byte = Byte('00000000')
        print(byte)
        assert byte.get_max_binvals() == 40320

        orig = byte.value
        # Flip bits then reverse and check the value to test things
        # are working correctly.
        update_animation(32, byte.increment, byte)
        update_animation(32, byte.decrement, byte)
        assert byte.value == orig
