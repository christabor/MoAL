# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class Luhn:
    @staticmethod
    def add_digits(digits):
        def multi(digit):
            if len(digit) > 1:
                return sum(map(int, list(digit)))
            return int(digit)
        return sum(map(multi, list(digits)))

    @staticmethod
    def checkdigit(digits):
        for k, digit in enumerate(digits):
            if k > 0 and k % 2 != 0:
                res = int(digit) * 2
                if res > 10:
                    # Sum the digits of the product if > 10
                    # (e.g 9 * 2 = 18; 1 + 8 = 9)
                    digits[k] = str(sum(map(int, list(str(res)))))
                else:
                    digits[k] = str(res)
        check_digit = sum(map(int, digits)) * 9
        digits = str(check_digit)
        last = len(digits) - 1
        return int(list(digits)[last])

    @staticmethod
    def test(number):
        digits = list(str(number))
        check_digit = Luhn.checkdigit(digits)
        _digits = []
        digits = list('{}{}'.format(number, check_digit))[::-1]
        for k, digit in enumerate(digits):
            _digit = str(int(digit) * 2) if k % 2 == 0 else digit
            _digits.append(_digit)
        # 7 9 9 2 7 3 9 8 7 1 3
        # 3 1 7 8 9 3 7 2 9 9 7
        # 3 2 7 16 9 6 7 4 9 18 7
        # 67 + 3
        # 70
        return Luhn.add_digits(_digits) % 10 == 0


if DEBUG:
    with Section('Luhn Algorithm'):
        # https://en.wikipedia.org/wiki/Luhn_algorithm

        test_nums = [
            79927398710,
            79927398711,
            79927398712,
            79927398713,
            79927398714,
            79927398715,
            79927398716,
            79927398717,
            79927398718,
            79927398719,
        ]

        for test in test_nums:
            print('Test: {} is {}'.format(test, Luhn.test(test)))
