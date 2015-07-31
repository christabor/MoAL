# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_simple
from MOAL.helpers.datamaker import subnet_mask
from MOAL.computer_organization import numerical_encoding_basic as encoders
from random import randrange as rr
from faker import Factory
from faker.providers import internet
from pprint import pprint as ppr


DEBUG = True if __name__ == '__main__' else False

faker = Factory.create()
faker.add_provider(internet)


class RoutingTable:

    def __init__(self):
        self.routes = []

    def __str__(self):
        ppr(self.routes)
        return ''

    def __getitem__(self, key):
        for route in self.routes:
            print(route, key)
            if key in route.values():
                return route

    def add(self, data):
        self.routes.append(data)

    def get_all(self, key):
        res = []
        for route in self.routes:
            res.append(route[key])
        return res

    def get_networkid(self, ip):
        """Network ID is comprised of Network Destination and Netmask,
        using CIDR notation. https://www.youtube.com/watch?v=t5xYI0jzOf4
        """
        entry = self[ip]
        mask = entry['network_mask']
        offset = 0
        # Add the octets as binary, then get the number of most significant
        # bits and add those to the end, to get the final CIDR encoded number.
        for octet in mask.split('.'):
            if octet == '255':
                offset += 8
            elif octet != '0':
                bits = encoders.dec_to_bin(int(octet))[0:4]
                for bit in bits:
                    if bit == '1':
                        offset += 1
        return '{}/{}'.format(entry['destination'], offset)

if DEBUG:
    with Section('Data structure - routing table'):
        rt = RoutingTable()

        # Values are randomly seeded and will not describe a
        # network topology appropriately, but are used for
        # illustrating the general idea.
        for n in range(4):
            # Create a test ip + random ips for using in code below
            ip = faker.ipv4() if n > 0 else '192.168.0.0'
            rt.add({
                'destination': ip,
                'network_mask': subnet_mask(),
                'gateway': faker.ipv4(),
                'interface': faker.ipv4(),
                'metric': rr(1, 10),
                'protocol': u'Local'
            })

        print(rt)
        print_simple('Destinations', rt.get_all('destination'))
        print_simple('Network Mask', rt.get_all('network_mask'))
        print_simple('Gateway', rt.get_all('gateway'))
        print_simple('Metrics', rt.get_all('metric'))
        print_simple('Network ID', rt.get_networkid('192.168.0.0'))

        _bin = encoders.dec_to_bin

        print('{} {} {} {}'.format(
            _bin(192),
            _bin(168),
            _bin(100),
            _bin(41)))
