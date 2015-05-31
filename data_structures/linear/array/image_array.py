# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from random import randrange
from random import random
from pprint import pprint as ppr

DEBUG = True if __name__ == '__main__' else False


class ImageArray(list):

    """Using an array as a means to represent an image - a nested array
    of RGBA values."""

    def __setitem__(self, key, pixel_data):
        self.insert(key, pixel_data)


def random_pixel():
    return [randrange(0, 255), randrange(0, 255),
            randrange(0, 255), round(random(), 1)]


if DEBUG:
    with Section('Image Array'):
        img = ImageArray()
        for n in xrange(10):
            img.insert(n, random_pixel())
        prnt('Random "pixel data" generated', img, func=ppr)
        print('...')
