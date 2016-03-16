"""Standard library FTP access."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from ftplib import FTP
import os


if DEBUG:
    with Section('FTP - Python stdlib'):
        # Read from it using stdlib - you can also use a
        # GUI FTP tool to test it, like FileZilla.
        ftp = FTP('127.0.0.1')
        res = ftp.login('chris', 'pass')
        print(res)
        assert res == '230 Login successful.'
        print(ftp.retrlines('LIST'))
        # Make a new file, where we know the FTP server is running.
        with open('/Users/chris/HELLOFTP.txt', 'wb') as newfile:
            newfile.write('\nHELLO FTP WORLD!')
        # Now go and retrieve it.
        res = ftp.retrbinary(
            'RETR HELLOFTP.txt', open('HELLOFTP.txt', 'wb').write)
        assert res == '226 Transfer complete.'
        # Also check its contents.
        with open(os.getcwd() + '/HELLOFTP.txt', 'rb') as xferfile:
            assert xferfile.read() == '\nHELLO FTP WORLD!'
