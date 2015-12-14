# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False

# A toy DSL for describing simple line "art"
program2 = """
@s => ~ 1...5
@d => ~~ * 20
@d => (+) x 10
@d => -- x 30
@w => "Well now..."
@d => * x 10
@w => "...hello to you"
@d => -- x 30
@d => (+) x 10
@d => ~~ * 20
@s => ~ 1...5
@w => "have a great night"
"""


if DEBUG:
    with Section('Metalinguistic Abstraction'):
        tokens = program2.split('\n')
        for token in tokens:
            if token != '':
                if token.startswith('@d => '):
                    subt = filter(
                        lambda x: x != '',
                        token.replace('@d => ', '').split(' '))
                    shape, _, amount = subt
                    print(shape * int(amount))
                elif token.startswith('@w => '):
                    subt = filter(
                        lambda x: x != '',
                        token.replace('@w => ', '').split(' '))
                    print(' '.join(subt).replace('"', ''))
                elif token.startswith('@s => '):
                    subt = filter(
                        lambda x: x != '',
                        token.replace('@s => ', '').strip().split(' '))
                    char, _range = subt
                    start, end = _range.split('...')
                    for x in range(int(start), int(end)):
                        print(char * (int(end) - x))
                    for x in range(int(start), int(end)):
                        print(char * x)
