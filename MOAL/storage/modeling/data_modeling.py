# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False

"""
From https://www.coursera.org/learn/data-manipulation/home/welcome
A Data Model is defined as having three primary properties:

1. Structure
  rows and columns
  nodes and edges
  key-value pairs
  sequence of bytes (raw, block data, file data)

2. Constraints
    "all rows must have the same number of columns"
    "all values in one column must have the same type"
    "a child cannot have two parents"

3. Operations
    "find value of key x"
    "find rows where column `lastname` is `jordan`"
    "get the next N bytes"
"""


class Structure:
    """This is a somewhat arbitrary and meaningless class, but it
    signifies some of these concepts in real code."""

    def __init__(self, *args, **kwargs):
        self.props = {}
        # Backup
        self.props['_schema'] = kwargs['schema']
        for kwarg, val in kwargs.iteritems():
            self.props[kwarg] = val

    def __getitem__(self, key):
        return self.props[key]

    def show_model(self):
        for val, val_type in self.props['schema'].iteritems():
            print('{}={}'.format(val, val_type))

    def constraint(self, constraint_name, field):
        print('CONSTRAINT: {} ... {}'.format(constraint_name, field))
        if constraint_name not in self.props['constraints']:
            raise ValueError(
                'Constraint {} does not exist!'.format(constraint_name))
        _args, _kwargs = field['args'], field['kwargs']
        return self.props['constraints'][constraint_name](*_args, **_kwargs)

    def operation(self, operation_name, val):
        print('OPERATION: {} ... {}'.format(operation_name, val))
        if operation_name not in self.props['operations']:
            raise ValueError(
                'Operation {} does not exist!'.format(operation_name))
        _args, _kwargs = val['args'], val['kwargs']
        return self.props['operations'][operation_name](*_args, **_kwargs)


# These constraints and operations are laid bare and can be used in classes,
# etc, as pure-ish functions.

# Operations

def create_field(schema, field, value):
    print('Schema OLD: {}'.format(schema[field]))
    schema[field] = value
    print('Schema NEW: {}'.format(schema[field]))


def read_field(schema, field):
    return schema[field]


def update_field(schema, field, replace):
    schema[field] = replace


def delete_field(schema, field):
    del schema[field]

# Constraints


def greater_than(val1, val2):
    return val1 > val2


def less_than(val1, val2):
    return val1 < val2


def longer(val1, val2):
    return str(val1) > str(val2)


def shorter(val1, val2):
    return str(val1) < str(val2)


if DEBUG:
    with Section('Data Modeling'):
        person = Structure(
            schema={'name': str, 'age': int},
            constraints={
                'lt': less_than,
                'gt': greater_than
            },
            operations={
                'create': create_field,
                'read': read_field,
                'update': update_field,
                'delete': delete_field,
            })
        person.show_model()
        person.operation('create',
                         {'args': (person['schema'], 'name', 'chris'),
                          'kwargs': {}})
        person.show_model()
        person.operation('update',
                         {'args': (person['schema'], 'name', 'christobot'),
                          'kwargs': {}})
        person.show_model()
        assert person['schema']['name'] == 'christobot'
        person.operation('create',
                         {'args': (person['schema'], 'lastname', 'taborium'),
                          'kwargs': {}})
