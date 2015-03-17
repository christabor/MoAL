# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from time import sleep
from helpers.display import Section
from helpers.display import print_h2
from helpers.display import divider
from helpers.text import random_byte as rand_byte
from computer_organization.one_twos_complement import ones_complement

DEBUG = True if __name__ == '__main__' else False
DELAY = 0.4

"""wikipedia.org/wiki/Bitwise_operation#Bitwise_operators

         (__)
       /   --      __\________/__
      |  /\_|     |  BinaryToday |
      |  |___     |   01101010   |
      |   ---@    |______________|
      |  |   ----   |          |
      |  |_____
*____/|________|>
*"""


def _show(bits, op, res):
    print('{} {} = {}'.format(bits, op, res))
    return res


def _show2(bits1, bits2, op, res):
    print('{}/{} {} = {}'.format(bits1, bits2, op, res))
    return res


def _checkbits(bits1, bits2):
    if len(bits1) != len(bits2):
        raise ValueError('Bit groups must be the same length!')


def bitwise_not(bits):
    """NOT is straightforward -  a simple one's complement will do,
    since the bits are merely flipped."""
    return _show(bits, 'NOT', ones_complement(bits))


def bitwise_and(bits1, bits2):
    """Do a logical AND on each pair of bits, by way of multiplication:
    e.g. 1 x 1 = 1, 0 x 0 / 0 x 1 = 0"""
    _checkbits(bits1, bits2)
    bits1, bits2 = list(bits1), list(bits2)
    before1, before2, res = ''.join(bits1), ''.join(bits2), ''
    for k, bit in enumerate(bits1):
        # Compare the bit indices
        bit1, bit2 = bits1[k], bits2[k]
        res += str(int(bit1) * int(bit2))
    return _show2(before1, before2, 'AND', ''.join(res))


def bitwise_or(bits1, bits2):
    """Do a logical OR on each pair of bits: e.g. 1/1 = 1, 0/1 = 1, 0/0 = 0"""
    _checkbits(bits1, bits2)
    bits1, bits2 = list(bits1), list(bits2)
    before1, before2, res = ''.join(bits1), ''.join(bits2), ''
    for k, bit in enumerate(bits1):
        bit1, bit2 = bits1[k], bits2[k]
        res += '0' if (bit1 == '0' and bit2 == '0') else '1'
    return _show2(before1, before2, 'OR', ''.join(res))


def bitwise_xor(bits1, bits2):
    """Do a logical OR on each pair of bits: e.g. 1/1 = 0, 0/1 = 1, 0/0 = 0"""
    _checkbits(bits1, bits2)
    bits1, bits2 = list(bits1), list(bits2)
    before1, before2, res = ''.join(bits1), ''.join(bits2), ''
    for k, bit in enumerate(bits1):
        bit1, bit2 = bits1[k], bits2[k]
        res += '1' if bit1 != bit2 else '0'
    return _show2(before1, before2, 'XOR', ''.join(res))


def test_operator_pairs(pairs, bitwise_op):
    """Test and assert two bit groups against the return value of given op"""
    for pair in pairs:
        b1, b2, res = pair
        assert bitwise_op(b1, b2) == res


"""wikipedia.org/wiki/Bitwise_operation#Bit_shifts"""


def _shift_left(bits):
    """Shift bits to the left <<<, carrying the bit over to the right;
    e.g. 0100 << 1000
    """
    bits = list(bits)
    # Append the least significant bit to the end.
    res = ''.join(bits[1:]) + bits[0]
    _show(''.join(bits), 'LEFT-SHIFT', res)
    return res


def _shift_right(bits):
    """Shift bits to the right >>>, carrying the bit over to the left,
    which preserves the sign; e.g. 0100 >> 0010
    """
    bits = list(bits)
    lsb = bits[-1]
    # Append the most significant bit to the beginning.
    res = lsb + ''.join(bits[:-1])
    _show(''.join(bits), 'RIGHT-SHIFT', res)
    return res


def _logical_shift_left(bits):
    bits = list(bits)
    res = ''.join(bits[1:]) + '0'
    _show(''.join(bits), 'LOGICAL LEFT SHIFT', res)
    return res


def _logical_shift_right(bits):
    bits = list(bits)
    res = '0' + ''.join(bits[:-1])
    _show(''.join(bits), 'LOGICAL RIGHT SHIFT', res)
    return res


def shift_right(bits, count=1, logical=False):
    for _ in range(count):
        if DEBUG:
            sleep(DELAY)
        bits = _logical_shift_right(bits) if logical else _shift_right(bits)
    return bits


def shift_left(bits, count=1, logical=False):
    for _ in range(count):
        if DEBUG:
            sleep(DELAY)
        bits = _logical_shift_left(bits) if logical else _shift_left(bits)
    return bits


def _shift_circular(bits):
    bits = list(bits)
    res = ''.join(bits[1:]) + bits[0]
    _show(''.join(bits), 'CIRCULAR SHIFT', res)
    return res


def shift_circular(bits, count=1):
    """A circular shift, where the ends are rotated; e.g. [0]10[1] > [1]10[0]"""
    for _ in range(count):
        if DEBUG:
            sleep(DELAY)
        bits = _shift_circular(bits)
    return bits


def rotate_through_carry(bits):
    """Like circular, but the end bits are stored as flags."""
    pass


if __name__ == '__main__':
    with Section('Computer organization - Bitwise operations'):
        assert bitwise_not('0111') == '1000'

        print_h2('Bitwise operations', desc='Wikipedia testing')
        # Testing examples from Wikipedia
        and_pairs = [('0110', '1101', '0100'), ('0101', '0011', '0001'),
                     ('0011', '0010', '0010'), ('0110', '0001', '0000')]
        or_pairs = [('0101', '0011', '0111'), ('0010', '1000', '1010')]
        xor_pairs = [('0101', '0011', '0110'), ('0010', '1010', '1000')]

        test_operator_pairs(and_pairs, bitwise_and)
        test_operator_pairs(or_pairs, bitwise_or)
        test_operator_pairs(xor_pairs, bitwise_xor)

        print_h2('Bitwise operations', desc='Randomly generated')

        for _ in range(5):
            pair = (rand_byte(), rand_byte())
            bitwise_not(pair[0])
            bitwise_and(*pair)
            bitwise_or(*pair)
            bitwise_xor(*pair)
            divider()

        print_h2('Bit-shifting', desc='Left shifts')

        left_shits = [('00010111', '00101110')]

        for shift in left_shits:
            bits, res = shift
            assert shift_left(bits) == res

        print_h2('Bit-shifting', desc='Right shifts')

        right_shifts = [('10010111', '11001011')]

        for shift in right_shifts:
            bits, res = shift
            assert shift_right(bits) == res

        # Multiple shifts
        assert shift_left('00010111', count=2) == '01011100'

        print_h2('Bit-shifting', desc='Logical shifts')

        assert shift_left('00010111', logical=True) == '00101110'
        assert shift_right('00010111', logical=True) == '00001011'

        print_h2('Bit-shifting', desc='Other shifts')

        assert shift_circular('00010111') == '00101110'

        shift_circular('00000101', count=6)
