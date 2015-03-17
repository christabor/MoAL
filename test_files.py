import os
import sys
import subprocess
from pprint import pprint as ppr
from glob import glob


BAD_FOLDERS = ['.git']
# BOGO sort is too slow to be worth testing.
BAD_FILES = ['__init__.py', 'bogo_sort.py', 'test_files.py']
EXPECTED_EXCEPTIONS = (NotImplementedError,)
# The actual error types we are looking out for.
UNEXPECTED_EXCEPTIONS = (IOError, ImportError, KeyError, AttributeError,
                         TypeError, IndexError)


def _get_all_files():
    paths = []
    start_dir = os.getcwd()
    pattern = "*.py"
    for root, dirs, files in os.walk(start_dir):
        paths.extend(glob(os.path.join(root, pattern)))
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
    return {'file': filepath, 'desc': desc, 'exception': exception.__name__}


if __name__ == '__main__':
    all_files = _get_all_files()
    test_results = []
    for filepath in all_files:
        filename = filepath.split('/')[-1]
        # if filename == 'quicktest.py':  # for quick debugging.
        if filename not in BAD_FILES:
            try:
                execfile(filepath)
            except EXPECTED_EXCEPTIONS:
                continue
            except UNEXPECTED_EXCEPTIONS:
                test_results.append(_result(filepath, sys.exc_info()))
    print('\nTEST RESULTS:')
    ppr(test_results)
