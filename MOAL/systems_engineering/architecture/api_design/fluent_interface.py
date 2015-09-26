# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import divider
from MOAL.helpers.datamaker import faker


DEBUG = True if __name__ == '__main__' else False


class ListMunger:

    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError
        self.data = sorted(data)

    def __str__(self):
        return '\n'.join(self.data)

    def add_values(self, values):
        self.data += values
        return self

    def filter_values(self, values):
        for k, v in enumerate(self.data):
            if v in values:
                self.data.pop(k)
        return self

    def filter_keys(self, keys):
        for k, v in enumerate(self.data):
            if k in keys:
                self.data.pop(k)
        return self


class Customer:

    def __init__(self):
        self.orders = {}
        self.active_order = None

    def __str__(self):
        f = ''
        for k, v in self.orders.iteritems():
            f += 'Order: #{}: {}\n'.format(k, v)
        return f

    def new_order(self, order_id, **order_data):
        self.orders[order_id] = order_data
        self.active_order = order_id
        return self

    def with_item(self, id, **item_data):
        self._active_order()['items'][id] = item_data
        return self

    def _active_order(self):
        return self.orders[self.active_order]

    def priority_rush(self):
        self._active_order()['rush'] = True
        return self


if DEBUG:
    with Section('Fluent Interface'):
        lmung = ListMunger([faker.name() for _ in range(10)] + ['Foo', 'Bar'])
        print(lmung)
        divider()
        lmung.filter_values(
            ['Foo', 'Bar']).filter_keys(range(2)).filter_keys(
                range(4)).add_values(['Baz', 'Quux']).filter_values(['Baz'])
        print(lmung)

        divider()
        cust = Customer()
        cust.new_order(
            92019,
            **{'name': 'awesome t-shirt', 'size': 'L'}).new_order(
                92020,
                **{'name': 'other awesome t-shirt', 'size': 'L'}).new_order(
                    92021,
                    **{'name': 'cooking pan', 'rush': False}).priority_rush()
        print(cust)
