# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
import random
import turtle

DEBUG = True if __name__ == '__main__' else False


def spiral(t, x_range=100, y_range=10):
    """Make a spiral."""
    for x in range(x_range):
        for y in range(y_range):
            t.forward(y / 4)
        t.left(x * 2)


def recursive_star(t, order, size, angles=[60, -120, 60, 120]):
    """Make a recursive, fractal-esque star."""
    if order is 0:
        t.forward(size)
    else:
        for angle in angles:
            recursive_star(t, order - 1, size / 3)
            t.left(angle)


def prog__growing_recursive_star(t):
    orig = 1
    while True:
        orig += random.randrange(0, 100)
        t.pen(pencolor='white', pensize=2)
        recursive_star(t, 2, orig)


def prog__schizophrenic_spiral(t, max_steps=100, size=10):
    def basic(t, max_range):
        for n in range(max_steps):
            t.forward(random.randrange(0, size + n + 1))
            t.left(random.randrange(0, size + n + 1))
            t.left(random.randrange(0, size + n + 1))
            t.left(random.randrange(-size + n + 1, size + n + 1))
            if n % 3 == 0:
                t.forward(random.randrange(0, size + n + 1))

    for step in range(max_steps):
        basic(t, step % 2 + 1)


if DEBUG:
    with Section('Fractal Geometry'):
        window = turtle.Screen()
        window.bgcolor('darkgreen')
        ella = turtle.Turtle()
        dad = turtle.Turtle()
        mom = turtle.Turtle()
        turts = [ella, dad, mom]
        map(lambda t: t.speed('fastest'), turts)
        # map(prog__growing_recursive_star, turts)
        map(prog__schizophrenic_spiral, turts)
