# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import cmd_title
from parsimonious.grammar import Grammar

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    with Section('Embedded Domain Specific Language (EDSL)'):
        print_h2('Parsing a grammar using the "parsimonious" library')
        button_grammar = Grammar(r"""
            btn = btn1 / btn2
            btn2 = "[" text "]"
            btn1 = "((" text "))"
            text = ~"[A-Z 0-9]*"i
            """)

        cmd_title('Printing [mybutton] and ((mybutton)) &', newlines=False)
        print(button_grammar.parse('[ mybutton ]'))
        print(button_grammar.parse('(( mybutton ))'))

        # Order matters - e.g. `tag` must come first, as it builds from the
        # previous tokens. This is obviously extremely naive, as it doesn't
        # check valid HTML-matching elements, nesting, single + wrapped
        # combos, attributes, etc....
        html = Grammar(r"""
            html = wrapped_tag+ / single_tag+
            wrapped_tag = opening content closing_wrapped
            single_tag = left content closing
            left = "<"
            right = ">"
            closer = "/"
            opening = left content right
            closing = closer right
            closing_wrapped = left closer content right
            text = ~"[A-Z 0-9]*"i / ""
            content = text / single_tag
            """)

        cmd_title('Printing <body>Content</body>', newlines=False)
        print(html.parse('<body>Content</body>'))
