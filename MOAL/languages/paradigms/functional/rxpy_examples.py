# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section, print_h2
from rx.internal import extensionmethod
from rx import Observable, AnonymousObservable, Observer
from rx.subjects import Subject
from logging.handlers import RotatingFileHandler
import logging
import string
import time


DEBUG = True if __name__ == '__main__' else False


@extensionmethod(Subject)
def fake_extensionmethod(self):
    print('[custom-extensionmethod] Observer: {}'.format(self))
    source = self

    def subscribe(observer):
        def on_next(x):
            pass
        return source.subscribe(
            on_next, observer.on_error, observer.on_completed)
    return AnonymousObservable(subscribe)


class TestObserver(Observer):

    def on_next(self, x):
        time.sleep(1)


class TestSubject(Subject):

    def on_next(self, x):
        print('[TEST subject] got: {}'.format(x))
        super(TestSubject, self).on_next(x)


class MyObserver(Observer):

    def on_next(self, x):
        print('Got: {}'.format(x))

    def on_error(self, x):
        print('Got error: {}'.format(x))

    def on_completed(self):
        print('Completed')


class LogWriterObserver(Observer):

    def __init__(self, *args, **kwargs):
        super(LogWriterObserver, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger('rxpy_logs')
        self.logger.addHandler(RotatingFileHandler('rxpy_logs'))
        self.logger.setLevel(logging.INFO)

    def on_next(self, x):
        self.logger.info('Got item: {}'.format(x))
        if x is None:
            raise Exception

    def on_error(self, x):
        self.logger.error('Got Error: {}'.format(x))

    def on_completed(self):
        self.logger.info('Completed -------------------------------------')


def _fmt(*args):
    return ''.join(map(str, args))


def _print(*args):
    print('got: {}'.format(_fmt(*args)))


def print_operator(x):
    print('[operator]: {}'.format(x))


def print_len3(x):
    print('`{}` is at least 3 characters long.'.format(x))


if DEBUG:
    with Section('Reactive (sort of functional) programming via RxPY'):
        print_h2('Basic Observable')
        xs = Observable.from_iterable(range(10) + [None])
        d = xs.subscribe(MyObserver())

        observable_iterable = Observable.from_iterable(xrange(100))
        logwriter = observable_iterable.subscribe(LogWriterObserver())
        print(logwriter)

        print_h2('Observable from_')
        xs = Observable.from_(range(10))
        gobbledygook = Observable.from_(list(string.punctuation))
        letters = Observable.from_(list(string.ascii_uppercase))
        merged = xs.merge(letters, gobbledygook).subscribe(_print)

        print_h2('Subjects')
        stream = TestSubject()
        stream.on_next(1)
        stream.on_next(2)
        d = stream.subscribe(_print)
        map(stream.on_next, range(5))
        stream.on_next(3)
        map(stream.on_next, range(5))
        stream.on_next(4)
        d.dispose()
        # Subclassed version prints, but the subscription object `d` does not
        stream.on_next(5)

        print_h2('Subjects + Operators')
        stream = Subject()
        stream.zip([1, 2, 3], ['a', 'b', 'c']).timestamp().scan('__scanned')
        stream.on_next(1)
        strm = stream.subscribe(print_operator)
        stream.on_next(2)
        strm.dispose()
        # Does not print, as subscriber with print function was disposed.
        stream.on_next(3)
        strm2 = stream.subscribe(print_operator)
        map(stream.on_next, range(10, 20))
        allstream = stream.filter(lambda value: len(value) > 3)
        allstream.subscribe(print_len3)
        stream.on_next('f')
        stream.on_next('ff')
        stream.on_next('fff')
        # Triggered
        stream.on_next('true')
        stream.on_next('fff')
        stream.on_next('ff')
        stream.on_next('f')
        # Triggered
        stream.on_next('truetrue')
