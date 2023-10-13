#!/usr/bin/python3
"""
Creating a function to print a square
"""


def print_square(size):
    """
    Prints a square using the '#' character

    Parameters:
    Size: the number of '#'

    Raises:
    TypeError: If size is not an integer or a float
    ValueError: if size is less than 0 or a float less than 0.
    """

    # Validate size

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)
    for _ in range(size):
        print('#' * size)
