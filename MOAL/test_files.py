"""Module for testing the entire project in various ways."""

import os
import subprocess
import sys

from glob import glob
from pprint import pprint as ppr

args = sys.argv

ADD_COVERAGE = '--cover' in args or '-c' in args
ADD_STATIC_ANALYSIS = '--static' in args or '-s' in args
TEST_FILES = '--test' in args or '-t' in args
TEST_CFG = '--cfg' in args or '-g' in args
BAD_FOLDERS = [
    '.git', 'bin', 'lib', 'python2.7',
    'docs', 'include', 'site-packages'
]
BAD_FILES = [
    '__init__.py',
    'get_file_tree.py',
    'bogo_sort.py',  # BOGO sort is too slow to be worth testing.
    'test_files.py',
    'queues_stdlib.py'  # Ignore multi-threaded files
]
EXPECTED_EXCEPTIONS = (NotImplementedError,)


def _get_all_files():
    paths = []
    start_dir = os.getcwd()
    pattern = "*.py"
    for root, dirs, files in os.walk(start_dir):
        globbed = glob(os.path.join(root, pattern))
        paths.extend(globbed)
    return paths


def _view_output_suppressed(popen_args=[]):
    """Optionally view suppressed output.
    A better alternative to subprocess.call()

    # Typical usage in this context: ['python', filepath]
    """
    popen = subprocess.Popen(
        popen_args, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = popen.communicate()
    exception = sys.exc_info()[1]
    return stdout, stderr, exception


def _result(filepath, exception_info):
    exception, desc, _ = exception_info
    exception = exception.__name__ if hasattr(exception, '__name__') else ''
    return dict(file=filepath, desc=desc, exception=exception)


def fmt_filename(path):
    """Format a filename from a given path."""
    parts = path.split('/')
    pyfile = parts[len(parts) - 1]
    pyfile = pyfile.replace('.py', '')
    return pyfile


if __name__ == '__main__':
    if not TEST_FILES or not ADD_COVERAGE:
        print('Nothing to do.')
    test_results = []
    dir = os.getcwd()
    for filepath in _get_all_files():
        print('========== [TESTING] Filepath: {}'.format(filepath))
        filename = filepath.split('/')[-1]
        if filename not in BAD_FILES:
            try:
                if TEST_CFG:
                    output = '{}/cfgs/{}.png'.format(
                        dir, filename.replace('.py', ''))
                    os.system(
                        'pycallgraph graphviz --output-file={} -- {}'.format(
                            output, filepath))
                if ADD_STATIC_ANALYSIS:
                    os.system('pylint {}'.format(filepath))
                if TEST_FILES:
                    execfile(filepath)
                if ADD_COVERAGE:
                    print('Getting coverage for: {}'.format(filepath))
                    # Add unique info for each file to combine with later.
                    os.system(
                        'coverage run --source=MOAL -p {}'.format(filepath))
            except EXPECTED_EXCEPTIONS:
                continue
            test_results.append(_result(filepath, sys.exc_info()))
    if ADD_COVERAGE:
        # Combine unique data and then generate report with it.
        os.system('coverage combine')
        os.system('coverage html -d coverage_report')
    if TEST_FILES:
        print('\nTEST RESULTS:')
        ppr(test_results)
