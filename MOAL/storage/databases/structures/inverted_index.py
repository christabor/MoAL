# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.generic import strip_punctuation
import requests
from collections import defaultdict

DEBUG = True if __name__ == '__main__' else False


def make_inverted_index(documents):
    """Make an inverted index of the words in a set of documents.

    Args:
        documents (dict): The name and list of documents.

    Returns:
        dict: The inverted index.
    """
    idx = defaultdict(set)
    for name, document in documents.iteritems():
        document = strip_punctuation(document)
        words = document.split()
        for word in words:
            idx[word].add(name)
    for word, docs in idx.iteritems():
        idx[word] = set(docs)
    return idx


if DEBUG:
    with Section('Inverted index'):
        docs = {}
        pages = [
            'https://en.wikipedia.org/wiki/Inverted_index',
            'https://en.wikipedia.org/wiki/Table_(database)',
            'https://en.wikipedia.org/wiki/Database_index',
            'https://en.wikipedia.org/wiki/Data_structure',
        ]
        for page in pages:
            docs[page] = requests.get(page).content
        idx = make_inverted_index(docs)
        for word, indices in idx.iteritems():
            print('"{}" in {}\n'.format(word, indices))
