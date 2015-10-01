# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


DEBUG = True if __name__ == '__main__' else False

# See https://en.wikipedia.org/wiki/Interface_segregation_principle for
# reference examples and definition.

# NOT SO SOLID


class MonsterATMClass:
    """A bad example of a large class handling everything."""

    def _validate(self, info):
        """Nonsense validation function"""
        if info is None:
            raise ValueError
        return True

    def calculate_balance(self, info):
        print('Calculating balance')

    def add_transaction_log(self, info):
        print(info)

    def handle_withdrawal(self, info, amt):
        self._validate(info)
        self.account_total -= amt
        self.add_transaction_log(info, amt, 'Withdrew {}'.format(amt))

    def handle_deposit(self, info, amt):
        self._validate(info)
        self.account_total += amt
        self.add_transaction_log(info, amt, 'Added {}'.format(amt))

    def print_receipt(self, info):
        print('Printing receipt...')

    def clear_info(self):
        print('Clearing info...')

    def add_fee(self, info, amt):
        print('Adding fee... {}'.format(amt))

    def authorize_pin(self, info):
        print('Authorizing...')


# SOLID

class ATMLogging:

    def add_transaction_log(self, info):
        print(info)

    def calculate_balance(self, info):
        print('Calculating balance')


class ATMAuthentication(ATMLogging):

    def _validate(self, info):
        """Nonsense validation function"""
        if info is None:
            raise ValueError
        return True

    def authorize_pin(self, info):
        print('Authorizing...')


class ATMWidthdrawl(ATMLogging):

    def handle_withdrawal(self, info, amt):
        self._validate(info)
        self.account_total -= amt
        self.add_transaction_log(info, amt, 'Withdrew {}'.format(amt))


class ATMDeposit(ATMLogging):

    def handle_deposit(self, info, amt):
        self._validate(info)
        self.account_total += amt
        self.add_transaction_log(info, amt, 'Added {}'.format(amt))


class ATMUserEvents(ATMLogging):

    def process_button(self, button_event):
        print('Handling button...')

    def clear_info(self):
        print('Clearing info...')

    def eject_card(self):
        print('Please take card')

    def print_receipt(self, info):
        print('Printing receipt...')
