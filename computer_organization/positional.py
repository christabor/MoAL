# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_h2
from helpers.display import print_h4
from computer_organization import numerical_encoding_basic as encoders

DEBUG = True if __name__ == '__main__' else False

# http://www.joelonsoftware.com/articles/Unicode.html

ALL_CHARS = list(unicode('0123456789abcdefghijklmnopqrstuvwxyz'
                         'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                         '.-:+=^!/*?&<>()[]{}@%$#'
                         'αβγδεζηθικλμνξóπϱστυφχψω', 'utf-8'))

BASES = [
    {'base': 2, 'name': 'Binary'},
    {'base': 3, 'name': 'Ternary'},
    {'base': 4, 'name': 'Quaternary'},
    {'base': 5, 'name': 'Quinary'},
    {'base': 6, 'name': 'Senary'},
    {'base': 7, 'name': 'Septenary'},
    {'base': 8, 'name': 'Octal'},
    {'base': 9, 'name': 'Nonary'},
    {'base': 10, 'name': 'Decimal'},
    {'base': 11, 'name': 'Undecimal'},
    {'base': 12, 'name': 'Duodecimal'},
    {'base': 13, 'name': 'Tridecimal'},
    {'base': 14, 'name': 'Tetradecimal'},
    {'base': 15, 'name': 'Pentadecimal'},
    {'base': 16, 'name': 'Hexadecimal'},
    {'base': 18, 'name': 'Octodecimal'},
    {'base': 20, 'name': 'Vigesimal'},
    {'base': 24, 'name': 'Tetravigesimal'},
    {'base': 25, 'name': 'Pentavigesimal'},
    {'base': 26, 'name': 'Hexavigesimal'},
    {'base': 27, 'name': 'Septemvigesimal'},
    {'base': 30, 'name': 'Trigesimal'},
    {'base': 32, 'name': 'Duotrigesimal'},
    {'base': 36, 'name': 'Hexatrigesimal'},
    {'base': 60, 'name': 'Sexagesimal'},
    {'base': 62, 'name': 'Duosexagesimal'},
    {'base': 64, 'name': 'Tetrasexagesimal'},
    {'base': 85, 'name': 'Pentaoctagesimal'},
    {'base': 120, 'name': 'Centovigesimal'},
    {'base': 240, 'name': 'Duocentoquadragesimal'},
    {'base': 360, 'name': 'Trecentosexagesimal'},
    {'base': 4, 'name': 'DNA - made up', 'custom': list('ATCG')},
    {'base': 4, 'name': 'RNA - made up', 'custom': list('AUCG')},
    # Novel examples from wikipedia.org/wiki/Binary_number#Representation
    {'base': 2, 'name': 'XO - made up', 'custom': list('XO')},
    {'base': 2, 'name': 'Morsish - made up', 'custom': list('|-')},
    {'base': 2, 'name': 'YesNo - made up', 'custom': list('yn')},
]


def n_to_dec(num, base, alphabet=None):
        """Convert a number to decimal from any given base, using the
        powers technique (e.g. 9203 = 9^3 + 2^2 + 0^1 + 3^0)

        Research examples from:
        www.cs.trincoll.edu/~ram/cpsc110/inclass/conversions.html"""
        # Reverse the digits and convert to list (e.g. 123 => ['3', '2', '1'])
        digits = list(reversed(unicode(num)))
        # Get 'parallel' indices for each digit.
        indices = reversed(range(0, len(digits)))
        total = 0
        for index in indices:
            # Get the current index of the number (e.g. 32[9]0)
            digit = digits[index]
            # Multiply by the current power (e.g. 9 * 2^3)
            result = int(digit) * base ** index
            # Add to running total
            total += result
            if DEBUG:
                print('B: {} I: {} Exp: {} * {} = {} Dec: {}').format(
                    digit, index, digit, base, result, total)
        print('Result: Base {} with value {} = {}'.format(base, num, total))
        return total


def dec_to_n(num, base, alphabet=None):
    """Convert a decimal to any base, using the divide by N technique.
    See `divide_by` for details."""
    result = ''
    divisisons = encoders.divide_by(num, base)
    for val in divisisons:
        try:
            # Use a custom alphabet if provided,
            # otherwise use the global set `ALL_CHARS`
            if alphabet is not None:
                result += alphabet[int(val)]
            else:
                result += ALL_CHARS[int(val)]
        except IndexError:
            result += str(val)
    print('{} base {} = {}'.format(num, base, result))
    return result


def test_base(base_info, nums=[4, 256, 512, 4096, 9999]):
    """Convert a base with a set of numbers, and display the results."""
    results = []
    for num in nums:
        if 'custom' in base_info:
            results.append(dec_to_n(num, base, alphabet=base_info['custom']))
        else:
            results.append(dec_to_n(num, base))
    return results


def dec_to_unary(num):
    """Tally representation e.g. | = 1, / = 5"""
    result = ''
    rounds = num // 5
    fives = 1
    if rounds < 5:
        result = '|' * num
    else:
        for round in range(0, rounds + 1):
            # Reset tally "five" marker every time it gets to five.
            if fives == 5:
                result += '/'
                fives = 0
            else:
                result += '|'
            fives += 1
    print_h4('Base 1', desc='aka "tally"')
    print('{} base 1 = {}'.format(num, result))


if DEBUG:
    with Section('Numerical encoding: "N-ary" (positional) - extended'):

        """I thought I had the extent of the positional number systems,
        but much more exist, and many can be found at:
        http://www.calculand.com/unit-converter/zahlen.php"""

        print_h2('N to Decimal', desc='Conversion to decimal from a given base')

        for n in range(4):
            print_h4('Convert base {}'.format(n))
            n_to_dec(999, n)

        print_h2(
            'Decimal to N',
            desc='Conversion of numbers to any base with divide-by technique.')

        for base_info in BASES:
            base, title = base_info['base'], base_info['name']
            print_h4('Base {}'.format(base), desc='aka "{}"'.format(title))
            test_base(base_info)

        for num in [4, 256, 512]:
            dec_to_unary(num)
