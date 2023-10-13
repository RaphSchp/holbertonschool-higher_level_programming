#!/usr/bin/python3
"""This is a module that contains a function

This function is going to be used to make the project of TDD
"""


def print_square(size):
    """Print a square with character '#'

    Args:
        size (int): The size of the square

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        print("#" * size, end="")
        print()
