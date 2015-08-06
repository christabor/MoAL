# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import firstcaps
from MOAL.helpers import datamaker as dm
from contextlib import contextmanager

DEBUG = True if __name__ == '__main__' else False


class FakeDatabaseError:
    pass


class FakeDatabase:

    def save(*args, **kwargs):
        print('Saving: {}, {}'.format(args, kwargs))
        return args, kwargs


@contextmanager
def orm_save(db_class, **kwargs):
    db = db_class()
    try:
        res = db.save(**kwargs)
        yield res
    except FakeDatabaseError:
        yield None


@contextmanager
def orm_save2(**data):
    print('Saving data... {}'.format(data))
    yield data
    print('Data saved!')


@contextmanager
def to_list(**data):
    html = '\n<ul>\n'
    for k, stuff in data.iteritems():
        if isinstance(stuff, str) and isinstance(stuff, str):
            k, stuff = firstcaps(k), firstcaps(stuff)
        html += '  <li><strong>{}</strong>: {}</li>\n'.format(k, stuff)
    html += '</ul>'
    yield html


class FakeDatabaseSaveHandler:

    def __init__(self, content):
        self.content = content

    def _print(self, data):
        print('Saved: {}'.format(data))

    def __enter__(self):
        print('Saving data: {}'.format(self.content))

    def __exit__(self, exception_type, exception_value, traceback):
        map(self._print, self.content)


if DEBUG:
    with Section('Context managers (aka "with")'):
        print_h2('[decorator] with 1 - database save wrapper, simplified')
        with orm_save(FakeDatabase, data={'my': 'fake-data'}) as saved:
            db, data = saved
            for k, data in data.iteritems():
                print('Yielded results: {}'.format(data))

        print_h2('[decorator] with 2 - database save wrapper, simplified')
        with orm_save2(foo='bar', bim='bam') as stuff:
            for data in stuff:
                print('Yielded results: {}'.format(data))

        print_h2('[decorator] nested context managers - save to db + show html')
        stuff = {
            'dna': dm.random_dna(max=20), 'faketrix': dm.random_binary_matrix()}
        with orm_save2(**stuff) as data, to_list(**data) as html:
            print('Saved all data, and converted to html: {}'.format(html))

        print_h2('[class] context manager - save to db + show html')
        with FakeDatabaseSaveHandler(stuff) as data:
            pass
