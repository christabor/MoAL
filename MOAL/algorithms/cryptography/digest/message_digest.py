# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_simple
from MOAL.helpers.display import print_h2
import tiger
import hashlib
import hmac

DEBUG = True if __name__ == '__main__' else False


if DEBUG:
    with Section('Message digest cryptography functions'):
        sekrit = 'A very very secret thing'
        print_h2('Hashlib algorithms')
        for algo in hashlib.algorithms:
            hashed = hashlib.new(algo).hexdigest()
            print_simple(algo, hashed, newline=False)

        print_h2('HMAC')
        _hmac = hmac.new('dxdstudio@gmail.com', sekrit)
        print(_hmac.hexdigest())

        _tiger = tiger.new(sekrit).hexdigest()
        print_simple('Tiger (TTH)', _tiger)
