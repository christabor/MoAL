# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_simple
import os

DEBUG = True if __name__ == '__main__' else False

"""
    en.wikipedia.org/wiki/Cohesion_(computer_science)
    For these examples, 'module' is actually considered a class.

    NOTE: some of these classes access properties or methods that do not exist.
    Making it fully compliant is irrelevant to the scope of this project.
    In some cases, the examples will work 100%, but some don't.
"""


class Utilities:
    """BAD, BAD, BAD! Grouping based on circumstance or coincidence."""

    def add_numbers(self, nums):
        return sum(nums)

    def get_fullname(self, user):
        return '{}. {} {}'.format(user.prefix, user.firstname, user.lastname)

    def format_thing(self, stuff):
        return 'Formatted: {}'.format(stuff)


class InputsController:
    """Grouping based on logical category of functionality or type"""

    def handle_keyboard(self, character):
        pass

    def handle_mouse(self, x, y):
        pass

    def handle_other(self, **kwargs):
        pass

    def register_input(self, name, **kwargs):
        pass


class ProcessUserData:
    """Grouping based on procedural and temporal:
    process -> _process -> handle -> error | success"""

    def process(self, **kwargs):
        data = self.handle_file()
        try:
            self.process_data(data)
            self.success('yay!')
        except ValueError:
            self.add_error('Some error!')

    def handle_file(self):
        pass

    def process_data(self):
        pass

    def success(self, msg):
        pass

    def add_error(self, msg):
        pass


class FileOpener:
    """Grouping based on procedure: open -> check perms -> read | error"""

    def __init__(self):
        self.access_permissions = {
            'read': ['bob', 'tim', 'angie', 'linda'],
            'write': ['linda', 'angie', 'bob'],
        }

    def open(self, user, filename):
        if self._can_read(user):
            return self.readfile(filename)
        else:
            self.add_error('Cannot read this file!')

    def _can_read(self, user):
        return user.name in self.access_permissions('read')

    def _can_write(self, user):
        return user.name in self.access_permissions('write')


class HandleUser:
    """Grouping based on operating on the same piece or type of data."""

    def create(self, user_id, **data):
        pass

    def read(self, user_id, **data):
        return self.store.read(user_id)

    def update(self, user_id, **data):
        self.store.read(user_id).update(**data).save()

    def delete(self, user_id):
        self.store.read(user_id).delete()


class UnixPipe:
    """Grouping based on the notion that outputs to one function become
    the input to another, when combined in sequence.
    This is the crux of the UNIX philosophy."""

    def __init__(self):
        self.data = None

    def ls(self):
        self.data = os.listdir(os.getcwd())
        return self

    def grep(self, keyword):
        for chunk in self.data:
            if keyword in chunk:
                self.data = chunk
        return self

    def save(self, filename):
        with open(filename, 'wb+') as newfile:
            newfile.write('>>> {}'.format(self.data))
        return self


class Lexer(object):
    """Grouping based on specific functions that contribute
    to a single, well-defined goal."""

    def __init__(self, wrapper_start, wrapper_end, token_start, token_end):
        self.wrapper_start = wrapper_start
        self.wrapper_end = wrapper_end
        self.start = token_start
        self.end = token_end

    def _fmt(self, token, k, count):
        return '  {}{}{}{}'.format(
            self.start, token, self.end, '\n' if k < count else '')

    def _fmt_wrapper(self):
        return self.wrapper_start + '\n{}\n' + self.wrapper_end

    def tokenize(self, string):
        tokens = string.split(' ')
        wrapper = self._fmt_wrapper()
        _tokens, count = '', len(tokens) - 1
        for k, token in enumerate(tokens):
            _tokens += self._fmt(token, k, count)
        return wrapper.format(_tokens)


class NaiveXMLLexer(Lexer):

    def __init__(self):
        super(NaiveXMLLexer, self).__init__(
            '<item>', '</item>', '<token>', '</token>')


class SExpressionLexer(Lexer):

    def __init__(self):
        super(SExpressionLexer, self).__init__('(', ')', '(', ')')


def _print(text, title, thing):
    members = [ref for ref in dir(thing)
               if not ref.startswith('__') and not ref.endswith('__')]
    print_simple('{} << {} >>'.format(
        text, title), [thing] + members, newline=False)

if DEBUG:
    with Section('GRASP High cohesion pattern'):
        _print('Bad!', 'Utilities (coincidental)', Utilities)
        _print('Inferior...', 'Inputs (logical)', InputsController)
        _print('Okay...', 'Processor (temporal)', ProcessUserData)
        _print('Okay...', 'File opener (procedural)', FileOpener)
        _print('Very good...', 'User (informational)', HandleUser)
        _print('Very good...', 'Pipe (sequental)', UnixPipe)
        _print('Best!', 'Parser (functional)', Lexer)

        """
        # Example usage of pipe...
        >>> pipe = UnixPipe()
        >>> pipe.ls().grep('TASKS.md').save('pipetest-123.txt')

        # Example usage of token...
        # luther = SExpressionLexer()
        # luther = NaiveXMLLexer()
        t = luther.tokenize('Do you know the story of Prometheus? No, of '
                            'course you don\'t. Prometheus was a god who stole '
                            'the power of fire from the other gods and gave '
                            'control of it to the mortals. In essence, he gave '
                            'us technology, he gave us power.')
        print(t)
        """
