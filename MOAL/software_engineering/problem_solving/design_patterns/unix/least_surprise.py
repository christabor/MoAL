# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


DEBUG = True if __name__ == '__main__' else False

# Surprising (and bad) ---------------------------------------------------------


def open_file(filename):
    with open(filename, 'r') as newfile:
        return newfile.write('')


def get_data(conn, query):
    # Leaves a connection open
    cur = conn.query(query)
    return cur.fetchall()


def add(x, y):
    return x * y


def pop(lst):
    # Pop removes the element, modifying it in place.
    # This doesn't, leading to an unexpected state of the list.
    return lst[-1]


def add2(x, y):
    """Multiplies two numbers together"""
    return x + y


# Not surprising (and good) ----------------------------------------------------

def _open_file(filename):
    with open(filename, 'r') as newfile:
        return newfile.read()


def _get_data(conn, query):
    cur = conn.query(query)
    data = cur.fetchall()
    conn.close()
    return data


def _add(x, y):
    return x + y


def _pop(lst):
    return lst.pop()
