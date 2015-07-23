# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_simple
from uuid import uuid1

DEBUG = True if __name__ == '__main__' else False


class InvoiceManager:
    """The invoice manager is another potential source of indirection.
    The customer manager should not know much about invoices, except
    how to delegate them via indirection, to the invoice manager.
    Simply operations like adding and retrieving,
    should be all the users of this manager should know."""

    def __init__(self):
        self.invoices = {}

    def get_all(self):
        return self.invoices

    def create(self, customer, amount):
        invoice = {
            'customer': customer['name'],
            'amount': amount,
            'id': 'TX{}'.format(uuid1())
        }
        if customer['id'] in self.invoices:
            self.invoices['id'].append(invoice)
        else:
            self.invoices[customer['id']] = [invoice]


class CustomerManager:
    """The customer manager acts as a layer of indirection to common
    operations that should not be cluttering up the actual customer object."""

    def __init__(self):
        self.customers = {}
        self.invoices = InvoiceManager()

    def __delitem__(self, name):
        del self.customers[name]

    def add_balance(self, customer, amount):
        name = customer.name
        cust = self.customers[name]
        cust['balance_due'] += amount

    def add(self, customer):
        self.__setitem__(customer.name, customer.details)

    def __setitem__(self, name, details):
        self.customers[name] = {
            'id': 'CU{}'.format(uuid1()),
            'name': name, 'details': details, 'balance_due': 0}

    def process_balances(self):
        for name, customer in self.customers.iteritems():
            print('Processing customer: #{} ({})'.format(customer['id'], name))
            if customer['balance_due'] > 0:
                print('Invoicing... {}'.format(customer['balance_due']))
                self.invoices.create(customer, customer['balance_due'])
            else:
                print('No balance due.')

    def get_invoices(self):
        print_simple('All invoices', self.invoices.get_all())


class Customer:

    def __init__(self, name, details):
        self.details = details
        self.name = name


if DEBUG:
    with Section('GRASP indirection/delegation pattern'):
        mgr = CustomerManager()
        bob = Customer('bob', {'age': 24})
        jane = Customer('jane', {'age': 32})
        eras = Customer('erasmus', {'age': 1010})

        mgr.add(bob)
        mgr.add(jane)
        mgr.add(eras)

        mgr.add_balance(eras, 9000.01)
        mgr.add_balance(bob, 120.00)
        mgr.process_balances()

        mgr.get_invoices()
