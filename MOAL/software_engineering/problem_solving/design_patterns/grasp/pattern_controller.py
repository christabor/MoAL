# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class DBConnectionError:
    pass


class DBReadError:
    pass


class MockDBAdapter:

    def __init__(self, *args, **kwargs):
        self.conn = {
            'name': '',
            'password': '',
            'name': None,
            'url': None
        }
        self.data = {}

    def rollback(self):
        print('Rolling back!')

    def commit(self):
        try:
            print('Committing...')
        except DBConnectionError:  # Not actually surfaced
            print('Could not commit!')
            self.rollback()

    def write(self, key, **kwargs):
        self.data[key] = kwargs
        print('Writing... `{}`'.format(key))
        for kwarg in kwargs:
            print('  |____ {}'.format(kwarg))

    def read(self, key):
        try:
            print('Reading... `{}`'.format(key))
            return self.data[key]
        except KeyError:
            raise DBReadError


class Controller(object):
    """en.wikipedia.org/wiki/GRASP_(object-oriented_design)#Controller"""

    def __init__(self, *args, **kwargs):
        if 'model' in kwargs:
            self.db = MockDBAdapter(kwargs['model'])
        else:
            self.db = MockDBAdapter()

    def receive(self, eventname, **data):
        raise NotImplementedError

    def send(self, eventname, data):
        raise NotImplementedError


class InvalidEvent:
    pass


class CustomerController(Controller):
    """MVC Style"""

    def send(self, event, **kwargs):
        if 'name' not in kwargs:
            raise ValueError('Name and/or data missing.')
        ops = {
            'create': self._create_user,
            'edit': self._edit_user,
            'read': self._read_user,
            'delete': self._delete_user,
        }
        try:
            return ops[event](**kwargs)
        except KeyError:
            raise InvalidEvent

    def _read_user(self, **kwargs):
        return self.db.read(kwargs['name'])

    def _create_user(self, **kwargs):
        self.db.write(kwargs['name'], **kwargs)
        self.db.commit()

    def _edit_user(self, **kwargs):
        user = self.db.read(kwargs['name'])
        if user is not None:
            self.db.write(kwargs['name'], **kwargs)
            self.db.commit()

    def _delete_user(self, name):
        pass


class InputController:

    def __init__(self):
        self.position = {
            'up': 0,
            'left': 0,
            'right': 0,
            'down': 0,
        }

    def _event(self, pos):
        self.position[pos] += 1
        print('Moving {}...'.format(pos))

    def push(self, button_name):
        """Another design principle here is indirection - the buttons
        should not be mapped to their internal states, as we might want
        to change button configurations for different users."""

        if button_name is 'w':
            self._event('up')
        elif button_name is 'a':
            self._event('left')
        elif button_name is 's':
            self._event('down')
        elif button_name is 'd':
            self._event('right')
        else:
            print('Invalid button! How did you manage that?!')

    def get_position(self):
        return self.position


if DEBUG:
    with Section('GRASP Controller pattern - MVC Style'):
        usermanager = CustomerController()
        usermanager.send('create', name='ctab', data={'foo': 'bar'})
        assert usermanager.send('read', name='ctab')['data']['foo'] is 'bar'

        usermanager.send('edit', name='ctab', data={'foo': 'bim'})
        assert usermanager.send('read', name='ctab')['data']['foo'] is 'bim'

    with Section('GRASP Controller pattern - Direct user behavior'):
        controller = InputController()
        controller.push('w')
        controller.push('a')
        controller.push('s')
        controller.push('d')
        print(controller.get_position())
