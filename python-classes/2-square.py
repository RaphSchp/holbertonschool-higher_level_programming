#!/usr/bin/python3
"""Square Class"""


class Square:

    """Square Class"""

    def __init__(self, size=0):
        """
            TypeError: `size` type is not `int`.

            ValueError:  `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
