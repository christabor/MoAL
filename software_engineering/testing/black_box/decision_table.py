# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_success
from helpers.display import print_error
from helpers.display import print_simple

DEBUG = True if __name__ == '__main__' else False


class DecisionTable:

    def __init__(self):
        self.count = 0
        self.actions = {}

    def __str__(self):
        print_simple('Actions', self.actions, newline=False)
        return ''

    def test(self, scenario):
        if scenario not in self.actions:
            raise ValueError('"{}" is an invalid scenario'.format(scenario))
        else:
            success, message = self.actions[scenario]
            message = '"{}" is {}: {} was "{}"'.format(
                scenario, 'not invalid' if not success else 'valid',
                'error' if not success else 'message', message)
            print_error(message) if not success else print_success(message)

    def __setitem__(self, scenario, result):
        if DEBUG:
            print(scenario.split(','))
        self.actions[scenario] = result


if DEBUG:
    with Section('Decision Tables and Decision Table Testing'):
        # Example table: "Signup form"
        dtt = DecisionTable()
        # Add actions - degenerate case - success
        dtt['user::Y, email::Y, pass::Y, pass2::Y'] = (True, 'Login attempt')
        # All other actions - failure
        dtt['user::Y, email::Y, pass::Y, pass2::N'] = (False, 'Bad pass2')
        dtt['user::Y, email::Y, pass::N, pass2::N'] = (False, 'Bad pass/pass2')
        dtt['user::N, email::Y, pass::Y, pass2::Y'] = (False, 'Bad user')
        dtt['user::N, email::N, pass::Y, pass2::Y'] = (False, 'Bad user/email')
        dtt['user::N, email::N, pass::N, pass2::Y'] = (
            False, 'Bad user/email/pass')
        dtt['user::Y, email::N, pass::N, pass2::N'] = (
            False, 'Bad email/pass/pass2')
        dtt['user::N, email::N, pass::N, pass2::N'] = (
            False, 'Bad usernmame/email/pass/pass2')

        dtt.test('user::N, email::N, pass::N, pass2::N')
        dtt.test('user::Y, email::Y, pass::Y, pass2::Y')
