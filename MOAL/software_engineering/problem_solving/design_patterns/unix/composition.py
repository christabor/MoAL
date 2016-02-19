"""
The UNIX Rule of Composition.

http://www.catb.org/esr/writings/taoup/html/ch01s06.html
"""
# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


def lquote(word):
    return '"{}'.format(word)


def rquote(word):
    return '{}"'.format(word)


def quotes(word):
    return lquote(rquote(word))


def exclaim(word):
    if word.endswith('\'') or word.endswith('"'):
        return '{}!{}'.format(word[0:-1], word[-1:len(word)])
    return '{}!'.format(word)


def emotify(word, emoticon):
    return '{} {}'.format(word, emoticon)


def sadface(word):
    return emotify(word, ':(')


def happyface(word):
    return emotify(word, ':)')


# Compose the above functions, or use them one-by-one as a user.
def quotehappy(word):
    return quotes(happyface(word))


def whosay(word, who='Me'):
    return '{} says {}'.format(who, quotes(word))


def chatsay(word, who='Anonymous'):
    return '**{}** says: {}'.format(who, quotes(word))


def chatsayhappy(word, who='Anonymous'):
    return chatsay(happyface(word), who=who)


if DEBUG:
    with Section('UNIX Rule of Composition'):
        f = quotes('Well Hello There')
        print(f)
        f = exclaim(f)
        print(f)
        print(happyface('Not sad'))
        print(sadface(quotes('Sadface')))
        print(quotehappy('Good day to you!'))
        print(whosay('How goes it?'))
        print(chatsay('I have arrived.'))
        print(chatsayhappy('I have arrived.'))
