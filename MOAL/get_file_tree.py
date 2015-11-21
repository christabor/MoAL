#!/usr/bin/env python

import os
import errno
import json
import sys


def valid(name):
    to_ignore = ['.git', '__init__.py', '.DS_Store']
    for item in to_ignore:
        if name.endswith(item):
            return False
    return True


def path_hierarchy(path):
    """
    CREDITS: http://unix.stackexchange.com/questions/164602/
        how-to-output-the-directory-structure-to-json-format
    """
    hierarchy = {
        'type': 'folder',
        'name': os.path.basename(path),
        'path': path,
    }
    try:
        hierarchy['children'] = [
            path_hierarchy(os.path.join(path, contents))
            for contents in filter(valid, os.listdir(path))
        ]
    except OSError as e:
        if e.errno != errno.ENOTDIR:
            raise
        hierarchy['type'] = 'file'
    return hierarchy


if __name__ == '__main__':
    try:
        directory = sys.argv[1]
    except IndexError:
        directory = '.'
    res = json.dumps(path_hierarchy(directory), indent=2, sort_keys=True)
    print(res)
