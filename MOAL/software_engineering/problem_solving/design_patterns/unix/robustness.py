# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


DEBUG = True if __name__ == '__main__' else False


class BasicCalculator:
    """All methods here have type checking in place so that bad inputs
    are automatically handled without throwing an error. This allows
    the behavior to be piped, etc, without any fatal error in behavior.
    """

    def div(self, nums):
        if not isinstance(list, nums):
            return 0
        res = 1
        for num in nums:
            res /= num
        return res

    def mult(self, nums):
        if not isinstance(list, nums):
            return 0
        res = 1
        for num in nums:
            res *= num
        return res

    def sub(self, num, subtrahend):
        if not isinstance(int, num) or not isinstance(int, subtrahend):
            return 0
        return num - subtrahend

    def add(self, nums):
        if not isinstance(list, nums):
            return 0
        return sum(nums)


class BasicCalculatorAlternate(BasicCalculator):
    """Another way to achieve this is to use kwargs with expected defaults,
    but this uses required args as kwargs, which are typically optional, and
    therefore not recommended."""

    def div(self, nums=[]):
        super(BasicCalculatorAlternate, self).div(nums)

    def mult(self, nums=[]):
        super(BasicCalculatorAlternate, self).mult(nums)

    def sub(self, num=1, subtrahend=0):
        super(BasicCalculatorAlternate, self).sub(num, subtrahend)

    def add(self, nums=[]):
        super(BasicCalculatorAlternate, self).add(nums)
