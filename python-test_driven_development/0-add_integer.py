#!/usr/bin/python3
"""
Function for adding two integers

"""


def add_integer(a, b=98):
    """Adds two integers.

    a: (int or float) first integer.
    b: (int or float) second interger. set to 98.

    Returns:
    sum of the two integers

    Raises:
    TypeError: if a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
