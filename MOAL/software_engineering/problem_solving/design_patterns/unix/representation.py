# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


DEBUG = True if __name__ == '__main__' else False


"""
Rule of Representation: Fold knowledge into data,
so program logic can be stupid and robust.

Source: http://www.catb.org/esr/writings/taoup/html/ch01s06.html

"Data is more tractable than program logic. It follows that where you see a
choice between complexity in data structures and complexity in code,
choose the former. More: in evolving a design, you should *actively* seek ways
to shift complexity from code to data."

Also see: http://www.catb.org/esr/writings/taoup/html/generationchapter.html
"""


def example_1_bad_method(arg):
    """This is convoluted and hard to read. It is also potentially
    less performant, since the logic branching must be generated and evaluated.
    """
    if arg is 'foo':
        return 1
    elif arg is 'bar':
        return 2
    elif arg is 'bim':
        return 3
    elif arg is 'bam':
        return 4
    elif arg is 'baz':
        return 5
    elif arg is 'quux':
        return 6


def example_1_good_method(arg):
    """This employees pure data, and is fast as it assumes a lookup, which is
    always O(N). The failed assumption is caught and handled, and new lookups
    can be quickly added, without adding much to the complexity."""
    data = {
        'foo': 1,
        'bar': 2,
        'bim': 3,
        'bam': 4,
        'baz': 5,
        'quux': 6,
    }
    try:
        return data[arg]
    except KeyError:
        return None


def example_2_bad_method(arg1, arg2):
    """Continuing down this path of complicated conditional branching,
    things get hairy very fast. Think about cognitive processing time when
    reading this code -- it's easy to make a mistake here."""
    if arg1 is 'foo' and arg2 is 'bar':
        return 1
    elif arg1 is 'bar' and arg2 is 'foo':
        return 3
    elif arg1 is 'foo' and arg2 is 'quux':
        return 2
    elif arg1 is 'bar' and arg2 is 'quux':
        return 4


def example_2_good_method(arg1, arg2):
    """Mapping inputs to this nested dictionary is easy and intuitive, compared
    to the more cognitively challenging task of parsing multiple levels of
    conditional branching statements. It is obvious almost immediately to look
    at the arguments and map them to the data and see what the result is.

    This is exemplified in the below quote from catb.org:

    "In Chapter 1 we observed that human beings are better at
    visualizing data than they are at reasoning about control flow."

    More advanced examples of this concept are discussed within the context of
    clojure s-expressions on the amazing "macronomicon" video by Michael Fogus:
    https://www.youtube.com/watch?v=0JXhJyTo5V8 this is not surprising to me
    because lisp-style languages are typically homoiconic, or nearly so, and so
    the code-as-data paradigm is commonplace for them.
    """
    data = {
        'foo': {
            'bar': 1,
            'quux': 2
        },
        'bar': {
            'foo': 3,
            'quux': 4
        }
    }
    try:
        return data[arg1][arg2]
    except KeyError:
        return None
