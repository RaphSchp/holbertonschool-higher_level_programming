#!/usr/bin/python3
"""This is a module that contains a function

This function is going to be used to make the project of TDD
"""


def add_integer(a, b=98):
    """Add two integers

    Both of the arguments must be integers or float. Otherwise raise
    an exception. If one of the numbers is type float, convert it to integer.

    Args:
        a (int, float): The first argument
        b (int, float): The second argument to add with a

    Returns:
        The sum of 'a' and 'b'

    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
