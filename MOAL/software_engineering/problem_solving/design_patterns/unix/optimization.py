"""UNIX Rule of Optimization: Prototype before polishing.
Get it working before you optimize it.

These are contrived examples, but they illustrate the point.
"""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


DEBUG = True if __name__ == '__main__' else False

# -----------------------------------------------------------------------------
# Building the basic code up from minimum working function to more robust
# This is GOOD


# Demonstrates the basic quick and dirty working version
def check_valid_strings_basic(vals):
    for val in vals:
        if not val:
            return False
    return True


# Demonstrates a slight improvement to type check and also a docstring.
def check_valid_strings_polish1(vals):
    """Checks for valid string values."""
    for val in vals:
        if val is None or len(val) == 0:
            return False
    return True


# Demonstrates everything above, but also adds docstring arguments
# for auto-documentation.
def check_valid_strings_polish2(vals):
    """Checks for valid string values.

    Args:
        vals (list): A list of values.
    Returns:
        is_valid: (bool): Boolean indicating whether all values were valid.
    """
    for val in vals:
        if val is None or len(val) == 0:
            return False
    return True


# -----------------------------------------------------------------------------
# Starting with all the bells and whistles, without even getting the basics.
# This is BAD
def bad_check_valid_strings_polish2(vals):
    """Checks for valid string values.

    Args:
        vals (list): A list of values.
    Returns:
        is_valid: (bool): Boolean indicating whether all values were valid.
    """
    is_valid = False
    for val in vals:
        print(val)
    return is_valid
