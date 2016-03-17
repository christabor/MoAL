"""Telnet example."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
import getpass
import sys
import telnetlib

HOST = 'localhost'
tn = telnetlib.Telnet(HOST)
user = raw_input('Enter your remote account: ')
password = getpass.getpass()
# Open connection right away
tn.open(HOST)

if DEBUG:
    with Section('Telnet example.'):
        if '--interact' in sys.argv:
            tn.interact()
        else:
            # Based off of https://docs.python.org/2/library/telnetlib.html
            tn.read_until('login: ')
            tn.write(user + '\n')

            if password:
                tn.read_until('Password: ')
                tn.write(password + '\n')
            tn.read_until('open\n')
            tn.write()
            tn.write('ls\n')
            tn.write('exit\n')
            print(tn.read_all())
