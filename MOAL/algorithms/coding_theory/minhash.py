# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import prnt
from random import randrange as rr


DEBUG = True if __name__ == '__main__' else False

"""See http://matthewcasperson.blogspot.com/2013/11/minhash-for-dummies.html
for a description of the steps required."""


def shingleify(pieces, offset=4):
    """Converts a sentence into "shingles" of length `offset`"""
    assert offset > 0
    pieces = list(pieces)
    shingles = []
    for k, piece in enumerate(pieces):
        _slice = pieces[k:k + offset]
        if len(_slice) >= offset:
            shingles.append(pieces[k: k + offset])
    return shingles


def hash_shingles(shingles):
    hashed = []
    for shingle in shingles:
        hashed.append(sum(map(hash_fnv1a, shingle)))
    return hashed


def hash_fnv1a(data):
    fnv_offset_basis = 14695981039346656037
    fnv_prime = 1099511628211
    hash = fnv_offset_basis
    for byte in data:
        byte = ord(byte)
        hash ^= byte
        hash *= fnv_prime
    return hash


def randoms(total):
    return [rr(1, 999) for _ in xrange(total)]


def rehash(hash, randoms):
    return [hash ^ n for n in randoms]


def jaccard_coefficient_naive(set1, set2):
    set1 = set(set1)
    set2 = set(set2)
    common = float(len(set1.intersection(set2)))
    total = sum(map(len, [set1, set2]))
    total = float(total)
    jaccard_coef = common / (total - common)
    print('Jaccard naive: {} / ({} - {}) = {} ({}%)'.format(
        common, total, common, jaccard_coef, jaccard_coef * 100))
    return jaccard_coef


def jaccard_coefficient(set1, set2):
    shingles = shingleify(list(set1) + list(set2))
    rounds = len(shingles) % 4
    coeffs = []
    for round in range(rounds):
        res = jaccard_coefficient_naive(
            shingles[round - 1], shingles[round])
        coeffs.append(res)
    coeff = 0
    if len(coeffs) > 0:
        coeff = max(coeffs)
    print('Jaccard - coeffs: {}, max coeff: {})'.format(coeffs, coeff))
    return coeff


def min_hash(set1, set2):
    shingles = shingleify(list(set1) + list(set2))
    hashes = hash_shingles(shingles)
    hash = None
    if len(hashes) > 0:
        hash = min(hashes)
    # Hash a second time with random numbers xor'd
    new_hashes = rehash(hash, randoms(len(hashes)))
    print('Hashes: {}'.format(new_hashes))
    return new_hashes


if __name__ == '__main__':
    with Section('Algorithms / coding theory - MinHash'):
        comparisons = (
            (['a', 'b', 'c'], ['a', 'b', 'c']),
            (['a', 'cool', 'cat'], ['a', 'cool', 'bat']),
            (['chair', 'desk', 'rug', 'keyboard', 'mouse'],
             ['chair', 'rug', 'keyboard']),
            (['cat', 'dog', 'rabbit'], ['dog', 'giraffe']),
            (['chair', 'desk', 'rug'], ['keyboard', 'mouse']),
            (['chair', 'rug', 'keyboard'], []),
        )

        for sets in comparisons:
            prnt('Testing:', sets)
            jaccard_coefficient_naive(*sets)
            jaccard_coefficient(*sets)
            min_hash(*sets)
