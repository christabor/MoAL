# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from random import choice
from numpy import array, dot, random

DEBUG = True if __name__ == '__main__' else False

"""
Most perception code taken
from https://blog.dbrgn.ch/2013/3/26/perceptrons-in-python/

Updates/additions:
    1. Cleaned up, made var names easier to understand, added comments.
    2. Added variable length vector for seed data
    3. Added AND perceptron.
    4. Added NOT perceptron.
"""

unit_step = lambda x: 0 if x < 0 else 1

# Create some training data
training_data_or = [
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 1),
    (array([1, 0, 1]), 1),
    (array([1, 1, 1]), 1),
]

training_data_and = [
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 0),
    (array([1, 0, 1]), 0),
    (array([1, 1, 1]), 1),
]

training_data_not = [
    (array([0]), 1),
    (array([1]), 0),
]


def run_perceptron(training_data):
    errors = []
    bias = 0.2
    steps = 100
    # Make the randomized vector length dynamic
    vector_length = len(training_data[0][0])
    # Get a random 3-vector between 0 and 1
    # e.g. [0.03249, 0.12452, 0.49032]
    # This is used as the starting point
    rand_vec3 = random.rand(vector_length)
    print('\nStarting seed vector: {}'.format(rand_vec3))

    for _ in xrange(steps):
        vec3, expected = choice(training_data)
        # Get the dot product of the randomized vector and the training vector
        result = dot(rand_vec3, vec3)
        # Get the offset of the expected and the unit step value
        offset = expected - unit_step(result)
        errors.append(offset)
        # Update the starting vector
        rand_vec3 += bias * offset * vec3

    # Run it for visualization of the progress
    for vec3, expected in training_data:
        result = dot(vec3, rand_vec3)
        print("{}: {} = {} (expected {})".format(
            vec3[:2], result, unit_step(result), expected))

if DEBUG:
    with Section('Perceptron'):
        # Depending on the number of `steps` set, this may not return the right
        # answer each time. Since the starting vector is random, if the step
        # count is too low, it may be entirely wrong. You can play around with
        # this and see where things go.
        run_perceptron(training_data_or)
        run_perceptron(training_data_and)
        # This one trains much faster, as the number of cases is halved.
        run_perceptron(training_data_not)
