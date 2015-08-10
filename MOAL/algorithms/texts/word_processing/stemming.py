# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


def suffix_strip(word):
    for suffix in ['ing', 'ed', 'ly']:
        if word.endswith(suffix):
            return word.replace(suffix, '')
    return word


if DEBUG:
    with Section('Stemming algorithms'):
        words = ['swimming', 'running', 'flying', 'slated', 'dated',
                 'absolutely', 'richly']
        # Simple, which causes invalid words.
        for word in words:
            print('{} => {}'.format(word, suffix_strip(word)))
        # See a separate project of mine:
        # https://github.com/Automotron/namebot
        #   /blob/master/namebot/normalization.py
        # for example of using the NLTK stemmer, which actually works well,
        # and implements multiple types.
