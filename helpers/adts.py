import operator
from display import Section
from display import _print
from random import shuffle


class strictlist(list):
    """A list that only allows certain primitive types
    (when subclassed), and adds some useful helper methods that are
    applied to all members in the list, for that primitive.
    """

    def __init__(self, items, valid_type=None):
        self._type = valid_type
        self.items = [member for member in items if self._valid(member)]

    def __setitem__(self, index, value):
        """Don't allow incorrect types to be added, but do so gracefully."""
        if self._valid(value):
            super(strictlist, self).__setitem__(index, value)
        return self

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.items)

    def _valid(self, val):
        return isinstance(val, self._type)

    def do(self, func, val=None):
        if val is None:
            self.items = [func(item) for item
                          in self.items if self._valid(item)]
        else:
            self.items = [func(item, val) for item
                          in self.items if self._valid(item)]
        return self

    def funcmaker(self, func, baseval):
        """Creates a closure that can be used
        later with map()'s value(s)"""

        def new_func(args):
            return func(baseval, args)
        return new_func


class strlist(strictlist):

    def __init__(self, *args):
        super(strlist, self).__init__(*args, valid_type=str)

    def copy(self, times):
        self.do(operator.mul, val=times)
        return self

    def add(self, chars):
        self.do(operator.add, val=chars)
        return self

    def up(self):
        def _upper(item):
            return item.upper()
        self.do(_upper)
        return self

    def lo(self):
        def _lower(item):
            return item.lower()
        self.do(_lower)
        return self

    def reverse(self):
        def _rev(item):
            return item[::-1]
        self.do(_rev)
        return self

    def shuffle(self):
        shuffle(self.items)
        return self

    def split(self):
        """Take each key and convert its chars into a sub array for each key"""
        def _split(item):
            return [_ for _ in item]
        self.do(_split)
        return self


class intlist(strictlist):

    def __init__(self, *args):
        super(intlist, self).__init__(*args, valid_type=int)

    def mod(self, base):
        self.do(operator.mod, val=base)

    def mul(self, multiplicand):
        self.do(operator.mul, val=multiplicand)
        return self

    def add(self, addend):
        self.do(operator.add, val=addend)
        return self

    def sub(self, subtrahend):
        self.do(operator.sub, val=subtrahend)
        return self

    def div(self, divisor):
        self.do(operator.div, val=divisor)
        return self

    def fact(self):
        def _fact(n):
            return n ** n
        self.do(_fact)


if __name__ == '__main__':
    with Section('Testing abstract data type extensions'):
        # Testing
        il = intlist([2, 3, 4])
        _print('ADT - int', (il, il.mul(100), il.add(10).div(4)))

        strs = strlist(['a', 'b', 'c'])

        _print('ADT - str up, copy, add', (
            strs, strs.up(), strs.copy(2).add('!!')))

        strs2 = strlist(['cat', 'dog', 'monkey'])

        _print('ADT - str up, shuffle, copy, reverse', (
            strs2, strs2.up(), strs2.copy(3).reverse().shuffle()))

        _print('ADT - str add, copy, up, add, shuffle', (
            strs2, strs2.add(' ').copy(3).up().add(':D').shuffle()))

        print('Testing strictness')

        strs3 = strlist([1, 2])  # Should be empty
        _print('ADT - str len 0', len(strs3))  # 0

        strs3 = strlist(['foo', 'bar', 'bim'])

        _print('ADT - str len 3', len(strs3))  # 3
