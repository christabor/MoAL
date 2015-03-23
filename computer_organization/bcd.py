# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import divider
from helpers.display import print_h4
from computer_organization import numerical_encoding_basic as encoders

DEBUG = True if __name__ == '__main__' else False


def dec_to_bcd_8421(num):
    """Convert a decimal to binary, and decompress into Binary Coded Decimal.
    Adds trailing bits to the left to enforce a 4-bit "nibble" on all digits.
    Uses 8421 notation [see wikipedia.org/wiki/Binary-coded_decimal]"""
    bcd, binary, decimals = '', '', ''
    for digit in str(num):
        binval = encoders.dec_to_bin(int(digit))
        binary += '{}{}'.format(binval, ' ' * (4 - len(binval) + 1))
        if len(binval) < 4:
            binval = binval.zfill(4)
        bcd += '{} '.format(binval)
        decimals += digit + (' ' * 4)
    print('Value = {}\nD {}\nB {}\nC {}'.format(num, decimals, binary, bcd))
    divider(atom='<')
    return bcd


if DEBUG:
    with Section('Numerical encoding: Binary Coded Decimal (BCD)'):
        print('D = Decimal, B = Binary, C = Binary Coded Decimal')
        nums = [
            1, 2, 4, 16, 32, 64, 128, 256, 512, 1024, 2048, 1234,
            12345, 123456, 1234567, 12345678, 123456789]
        print_h4('BCD', desc='8421 encoding')
        for num in nums:
            dec_to_bcd_8421(num)
