# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_h4
from helpers.display import print_vars

DEBUG = True if __name__ == '__main__' else False

hexvals = list('0123456789abcdef')
HEX_VALS = {hexval: k for k, hexval in enumerate(hexvals)}
HEX_INTEGERS = {k: hexval for k, hexval in enumerate(hexvals)}


def _scale(base, maximum):
    """Creates a range of numbers up to `maximum`, given a base.
    This scale is used for visually converting numbers,
    and serves as an intuitive reference.

    See youtube.com/watch?v=e3mCABVEK88 for some good examples.

    e.g.

    ... 128     64     32     16     8     4     2     1
    ----------------------------------------------------
    Note: visual order is reversed, but not list.
    """
    value, values = base, [1]
    for k in range(maximum):
        values.append(value)
        value *= base
    return values, '{}\n{}'.format('     '.join(
        map(str, reversed(values))), '-' * 80)


def make_groups(string, count):
    """Make a set of groups with a string.

    e.g. >>> make_groups('ABCDEFGH', 2) = [['AB', 'CD', 'EF', 'GH']]
    Raises ValueError if modulus operation results in uneven group distribution.
    """
    groups = []
    if count == 0:
        return [string]
    if len(string) % count != 0:
        raise ValueError(
            'Modulus `{}` on string `{}` of length `{}` is not uniform.'.format(
                count, string, len(string)))
    else:
        for k in range(0, len(string), count):
            groups.append(string[k: k + count])
    if DEBUG:
        print_vars(['called via `make_groups`', groups])
    return groups


# ------------- CONVERTERS -----------------------------------------------------

def _divide_by(number, base):
    number = int(number)
    """General purpose numeral converter,
    using the divide-by N + modulo technique."""
    vals = []
    if base == 1:
        return [number]
    while number > 0:
        # Remainder = least significant bit
        val = number % base
        number = number // base
        # Add a new bit at the beginning for each increment
        vals.insert(0, str(val))
    return vals


def dec_to_hex(number):
    """Convert integer to hexadecimal"""
    hexnumber = ''
    for num in _divide_by(number, 16):
        hexnumber += HEX_INTEGERS[int(num)]
    return '0x{}'.format(hexnumber)


def dec_to_bin(number):
    """Convert integer to binary. Only handles positive integers."""
    if number < 0:
        raise TypeError
    bits = _divide_by(number, 2)
    for k, bit in enumerate(bits):
        # Pad digits if necessary
        bits[k] = bit.zfill(1)
    res = ''.join(bits)
    if DEBUG:
        print_vars([['dec', number], ['dec => bin', res]], convert=True)
    return res


def oct_to_dec(number):
    """Convert an octal to integer.
    algorithm/notes from robotroom.com/NumberSystems4.html
    """
    octal, index, digits = 0, 0, str(number)
    powers = list(reversed(range(len(digits))))
    for digit in digits:
        power = powers[index]
        res = int(digit) * 8 ** power
        print('Octal to dec: {} * 8^{} = {} * {} = {}'.format(
            digit, power, digit, 8 ** power, res))
        octal += res
        index += 1
    return octal


def oct_to_bin(number):
    """Convert octal to binary
    instructions used for algorithm from:
    wikipedia.org/wiki/Octal#Octal_to_binary_conversion
    """
    binary = ''
    digits = str(number)
    for digit in digits:
        print_vars(['octal digit', digit])
        binary += dec_to_bin(int(digit)).zfill(3)
    if DEBUG:
        print_vars(['octal to binary', binary])
    return binary


def dec_to_oct(number):
    """Convert an integer to an octal, using 'divide by base' technique."""
    return ''.join(map(str, _divide_by(number, 8)))


def bin_to_dec(number):
    """Convert binary to integer"""
    if not isinstance(number, str):
        number = str(number)
    if(number.startswith('0b')):
        number = number[2:]
    # Reverse the bits to make right side comparison easier with the co-domain
    bits = list(reversed(number))
    length = len(bits)
    value = 0
    # Map the binary number and co-domain 1:1 to see if the bits are
    # on or off, and add the corresponding number if so.
    codomain, _ = _scale(2, length)
    for index in range(length):
        if bits[index] == '1':
            value += codomain[index]
    return value


def bin_to_oct(binary):
    """Convert binary to octal.
    Uses integer conversion as an intermediate step."""
    octal = ''
    bin_groups = make_groups(binary, 3)
    for bin_group in bin_groups:
        octal += str(bin_to_dec(bin_group))
    if DEBUG:
        print('Binary {} to octal: {}'.format(binary, octal))
    return int(octal)


def bin_to_hex(number):
    """Convert binary to hexadecimal.
    Uses integer conversion as an intermediate step."""
    if isinstance(number, int):
        number = str(number)
    return dec_to_hex(bin_to_dec(number))


def oct_to_hex(octnumber):
    """Convert octal to hexadecimal.
    Uses binary conversion as an intermediate step.
    Instructions used for algorithm from:
    wikipedia.org/wiki/Octal#Octal_to_hexadecimal_conversion
    """
    hexnumber, binary = '', ''
    digits = str(octnumber)
    for digit in digits:
        # Convert decimal to binary, pad where appropriate.
        if digit == '0':
            binnumber = '000'
        elif digit == '1':
            binnumber = '001'
        else:
            binnumber = dec_to_bin(int(digit))
        binnumber = binnumber.zfill(2)
        binary += binnumber
    # Group remainder by 4 digits
    bin_groups = make_groups(binary, 4)
    if DEBUG:
        print_vars(
            [['bin group x 4', bin_groups], ['oct => hex (bin)', binary]])
    for group in bin_groups:
        # Add number, shave off individual 0x part from individual conversion.
        hexnumber += str(bin_to_hex(group))[2:]
    return '0x{}'.format(hexnumber)


def hex_to_dec(hexnumber):
    """Convert hexadecimal to integer"""
    hexnumber = str(hexnumber)
    if hexnumber.startswith('0x'):
        hexnumber = hexnumber[2:]
    value = 0
    length = len(hexnumber)
    codomain, _ = _scale(16, length)
    for k, val in enumerate(reversed(hexnumber)):
        val = HEX_VALS[str(val)]
        if DEBUG:
            print('{} * {} = {}'.format(val, codomain[k], val * codomain[k]))
        # Get the index that corresponds to the hex system
        value += val * codomain[k]
    if DEBUG:
        print('Hex 0x{} to int = {}'.format(hexnumber, value))
    return value


def hex_to_bin(hexnumber):
    """Convert hexadecimal to binary"""
    binary = dec_to_bin(hex_to_dec(hexnumber))
    if DEBUG:
        print_vars(['Hex to bin', binary])
    return binary


def hex_to_oct(hexnumber):
    """Convert hexadecimal to octal"""
    hexnumber = str(hexnumber)
    if hexnumber.startswith('0x'):
        hexnumber = hexnumber[2:]
    octal = ''
    binary = '0' + hex_to_bin(hexnumber)
    groups = make_groups(binary, 3)
    if DEBUG:
        print_vars(['Hex to octal', binary])
        print_vars(['Hex to octal (binary groups)', groups])
    for group in groups:
        octal += str(bin_to_oct(group))
    return int(octal)


# ------------- TESTING --------------------------------------------------------

def compare_to_native(
        native, custom, count=20, assert_results=False,
        prefix=None, supress_other=True):
    """Compares custom callable to the native version with a list of numbers."""
    print('Running func: {}'.format(native))
    failures = []
    if supress_other:
        global DEBUG
        DEBUG = False
    for n in range(1, count):
        res_n, res_c = native(n), custom(n)
        if prefix is not None:
            res_c = '{}{}'.format(prefix, res_c)
        print('native {}, mine {}'.format(res_n, res_c))
        if assert_results:
            try:
                assert res_n == res_c
            except AssertionError:
                failures.append([res_n, res_c])
    if assert_results:
        print('{}/{} failures'.format(len(failures), count))
        return failures


def genr():
    # General purpose conversion
    powers_mult(2, 9)
    powers_mult(10, 10)
    powers_ten(2048)
    powers_ten(1024)
    powers_ten(8)
    all_powers_two(0)
    all_powers_two(1)
    all_powers_two(2)
    all_powers_two(123)
    all_powers_n(0, 12)
    all_powers_n(1, 12)
    all_powers_n(2, 12)
    all_powers_n(144, 12)
    for n in range(2, 21):
        print('Base: {} | {}'.format(n, _scale(n, 4)[1]))
    # utility
    for n in range(2, 10):
        try:
            make_groups('001010111100', n)
        except ValueError:
            continue


def bina():
    assert '0b' + dec_to_bin(3029) == str(bin(3029)) == '0b101111010101'
    assert '0b' + dec_to_bin(12) == str(bin(12)) == '0b1100'
    assert '0b' + hex_to_bin('0x13e') == bin(0x13e) == '0b100111110'
    assert '0b' + oct_to_bin(51) == '0b101001'
    compare_to_native(bin, dec_to_bin, assert_results=True, prefix='0b')


def octa():
    assert bin_to_oct('001010111100') == 1274
    assert hex_to_oct('3fa5') == 37645
    assert dec_to_oct(4635) == '11033'
    assert dec_to_oct(12) == '14'
    assert dec_to_oct(390) == '606'
    assert dec_to_oct(500) == '764'
    compare_to_native(oct, dec_to_oct, assert_results=True, prefix='0')


def deca():
    assert int(0x13e) == hex_to_dec('0x13e') == 318
    assert int(0b10110111) == bin_to_dec('10110111') == 183
    assert oct_to_dec(345) == 229
    assert oct_to_dec(112) == 74


def hexa():
    assert oct_to_hex(345) == '0xe5'
    assert oct_to_hex(1057) == '0x22f'
    assert dec_to_hex(906) == '0x38a'
    assert dec_to_hex(1792) == '0x700'
    assert bin_to_hex('01011110101101010010') == '0x5eb52'
    assert bin_to_hex('11011001') == '0xd9'
    compare_to_native(hex, dec_to_hex, assert_results=True)


# ------------- MISC. FUN STUFF ------------------------------------------------


def all_powers_n(number, power):
    """Powers of two check, extended to any exponent"""
    powers = []
    while number > 1:
        # Starting from largest to smallest is significantly faster
        for n in reversed(range(12)):
            product = power ** n
            # 2^12 covers many cases, but doesn't cover a lot of larger numbers;
            # this demonstration is just a basic primer on the algorithm.
            if product < number:
                print('{}^{} ... (|{} - {}| = {})'.format(
                    power, n, number, product, number - product))
                number -= product
                powers.append(n)
    return powers


def all_powers_two(number):
    """Find the various powers of two for a given number -- often used
    for finding binary number values of a number, since is base 2."""
    return all_powers_n(number, 2)


def powers_mult(number, power):
    """Visualization of all values of a number raise up to a max power."""
    for n in range(power):
        mult_val = ' x '.join([str(number) for _ in range(n)])
        print('{}^{} = {} = {}'.format(number, n, mult_val, number ** n))


def powers_ten(number):
    """A visualization of the powers of ten technique for numbers"""
    value = 0
    digits = list(reversed(str(number)))
    places = len(digits)
    values = []
    mapping = {}
    for index in reversed(range(places)):
        place_index = '1{}'.format('0' * index)
        place = int(digits[index]) * int(place_index)
        value += place
        values.append(place)
        mapping[place] = (int(digits[index]), int(place_index))
        print('{} * {} = {}'.format(digits[index], place_index, place, value))
    print('{} = {}'.format(' + '.join(map(str, values)), number))
    print('\n')
    return mapping


if DEBUG:
    with Section('Computer organization - Numerical encoding'):
        groups = {
            'General': genr,
            'Hexadecimal': hexa,
            'Octal': octa,
            'Binary': bina,
            'Decimal': deca,
        }
        for title, func in groups.iteritems():
            print_h4(title, desc='The {} encoding scheme.'.format(title))
            func()
