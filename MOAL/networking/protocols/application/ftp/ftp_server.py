"""FTP Server to test against."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import sys

ADMINS = False
SERVER_URI = '127.0.0.1'
PERMS = 'elradfmw' if ADMINS else 'elramw'

if DEBUG:
    with Section('FTP - Server'):
        # Serving our own
        servdir = sys.argv[2] if '--serve' in sys.argv else '/Users/chris/'
        authorizer = DummyAuthorizer()
        # http://pythonhosted.org/pyftpdlib/api.html?highlight=permissions
        authorizer.add_user('chris', 'pass', servdir, perm=PERMS)
        authorizer.add_anonymous(servdir)
        handler = FTPHandler
        handler.authorizer = authorizer
        server = FTPServer((SERVER_URI, 21), handler)
        server.serve_forever()
