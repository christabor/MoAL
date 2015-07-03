# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""


import os
import sys
from glob import glob

sys.path.append(os.getcwd())

"""Automatically adds all __init__.py files to all subdirectories
that do not already have it."""


def write_init(newpath):
    with open(newpath, 'wb+') as initfile:
        initfile.write('\n')


def modulify():
    paths = []
    start_dir = os.getcwd()
    pattern = "*.py"
    for dir, subdirs, files in os.walk(start_dir):
        if '.git' not in dir:
            if '__init__.py' not in files or len(dir) == 0:
                newpath = '{}/__init__.py'.format(dir)
                write_init(newpath)
        paths.extend(glob(os.path.join(dir, pattern)))
    return paths


modulify()
