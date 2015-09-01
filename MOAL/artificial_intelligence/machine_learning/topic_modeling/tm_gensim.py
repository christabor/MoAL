# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from pyquery import PyQuery as Pq
from gensim import corpora
from gensim import models
from gensim import similarities
from string import punctuation
from nltk.corpus import stopwords
from collections import defaultdict
from pprint import pprint as ppr
import logging
import os

DEBUG = True if __name__ == '__main__' else False
stop = stopwords.words('english') + ['i.e.', 'e.g.']
path = os.path.dirname(__file__)

LOGGING = False

if LOGGING:
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s',
        level=logging.INFO)


def get_random_site():
    return Pq(url='http://www.randomwebsite.com/cgi-bin/random.pl')


def get_random_sites(total):
    return [Pq(get_random_site()).html().split('\n') for _ in range(total)]


def get_docs(files):
    """
    Usage:
        >>>> get_docs(['foo.txt', 'bam.txt', 'quux.text'])
        [Dictionary(), Dictionary(), ...]
    """
    doc_dicts = []
    for _file in files:
        _dict = corpora.Dictionary(line.lower().split() for line in open(_file))
        doc_dicts.append(_dict)
    return doc_dicts


def get_frequency(docs):
    d = defaultdict(int)
    for doc in docs:
        for token in doc:
            d[token] += 1
    # filter < 1
    d2 = {token: count for token, count in d.iteritems() if count > 1}
    return d2


def clean_token(token):
    token = token.lower()
    for piece in ['\n', '\t', ''] + list(punctuation):
        token = token.replace(piece, '')
    return token


def get_tokens(line):
    tokens = []
    for token in line.split(' '):
        if token not in stop and token != '':
            tokens.append(clean_token(token))
    return tokens


def get_filetokens(name):
    tokens = []
    with open('{}/{}'.format(path, name)) as filedata:
        for line in filedata.readlines():
            tokens += get_tokens(line)
    return tokens


class TopicModeler:

    def __init__(self, tokens):
        self.tokens = tokens
        # Index is used for querying, and must be built.
        self.index = None
        self.transformation = None
        self.vectors = None
        # Create the gensim topic dictionary object for use as we move forward
        self.dictionary = corpora.dictionary.Dictionary(self.tokens)

    def __iter__(self):
        for token in self.tokens:
            yield token

    def frequency(self):
        return get_frequency(self.tokens)

    def compactify(self):
        return self.dictionary.compactify()

    def xform_tfidf(self):
        self.transformation = models.TfidfModel(self.get_vectors())

    def _xform(self):
        if self.transformation is None:
            self.xform_tfidf()

    def tfidf(self, *vector_indices):
        self._xform()
        return self.transformation[vector_indices]

    def re_index(self):
        self._xform()
        self.index = similarities.SparseMatrixSimilarity(
            self.transformation[self.get_corpus()], num_features=4)

    def get_vectors(self):
        if self.vectors is None:
            self.vectors = [self.dictionary.doc2bow(doc) for doc in self.tokens]
        return self.vectors

    def get_corpus(self):
        return self.get_vectors()

    def get_xform(self):
        self._xform()
        return self.transformation

    def get_index(self):
        if self.index is None:
            self.re_index()
        return self.index

    def check_similary(self, doc, lsi):
        vec_bagofwords = self.dictionary.doc2bow(doc)
        # convert the query to LSI space
        vec_lsi = lsi[vec_bagofwords]
        # print(vec_lsi)
        index = similarities.MatrixSimilarity(lsi[corpus])
        return index[vec_lsi]


if DEBUG:
    with Section('Topic Modeling'):

        doc_tokens = [get_filetokens('topic{}.txt'.format(
                      filenum)) for filenum in range(1, 5)]

        tm = TopicModeler(doc_tokens)

        print_h2('Token frequency')
        ppr(tm.frequency())

        # Compact tokens, scoring and remove empty values
        tm.compactify()

        print_h2('Token ID and bag-of-word as vectors')
        # Convert the document to a vector of ID and bag-of-words
        vectors = tm.get_vectors()
        print(vectors)

        # print_h2('Show (lockstep), the vectors and corresponding docs')
        # for k, doc in enumerate(doc_tokens):
        #     print('{} {}'.format(vectors[k], doc))

        print_h2('Token IDs (via `token2id`)')
        # Show the tokens and ids
        ppr(tm.dictionary.token2id)

        print_h2('Adding a new "document"')
        new_doc = get_tokens('Computers rule, typewriters drool')
        new_vec = tm.dictionary.doc2bow(new_doc)
        ppr(new_vec)

        print_h2('Change vector representation to TFIDF')

        vec = [(0, 1), (4, 1)]
        ppr(tm.tfidf(vec))

        # xform = tm.get_xform()
        # tm.re_index()
        # index = tm.get_index()
        # sims = index[xform[vec]]
        # print(list(enumerate(sims)))

        corpus = tm.get_corpus()
        dictionary = tm.dictionary
        lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

        # Similarity querying ------------

        new_docs = ['Hello, good day',
                    'Computer Science and STEM', 'Nothing relevant']

        for doc in new_docs:
            sim = tm.check_similary(
                'Computer science degrees'.lower().split(), lsi)
            print(sim)
