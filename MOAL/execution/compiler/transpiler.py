# -*- coding: utf-8 -*-

"""A markdown to python transpiler."""

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

IS_MAIN = True if __name__ == '__main__' else False

if IS_MAIN:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from collections import namedtuple

from MOAL.helpers.display import Section


Heading = namedtuple('Heading', 'number value tag')
Tag = namedtuple('Tag', 'name value tag')


def transpile_md_to_python(markdown):
    """A very naive markdown to python converter."""
    for line in markdown.split('\n'):
        line = line.lstrip()
        if line.startswith('# '):
            yield Heading(1, line, 'h1')
        elif line.startswith('## '):
            yield Heading(2, line, 'h2')
        elif line.startswith('### '):
            yield Heading(3, line, 'h3')
        elif line.startswith('#### '):
            yield Heading(4, line, 'h4')
        elif line.startswith('##### '):
            yield Heading(5, line, 'h5')
        elif line.startswith('###### '):
            yield Heading(6, line, 'h6')
        elif line.startswith('*') and not line.endswith('**'):
            yield Tag('emphasis', line, 'em')
        elif line.startswith('**') and line.endswith('**'):
            yield Tag('strong', line, 'strong')
        elif line.startswith('[') and line.endswith(')'):
            yield Tag('href', line, 'a')

if IS_MAIN:
    with Section('Bytecode interpreter'):
        markdown = """
        # Hello
        I am a paragraph of text
        #### Hello 4
        ## Hello 2
        ### Hello 3
        ###### Hello 6
        ##### Hello 5

        *Hello*

        **Hello!**

        [I'm a single line link!](Some URL)
        """

        transd = transpile_md_to_python(markdown)
        print(list(transd))
