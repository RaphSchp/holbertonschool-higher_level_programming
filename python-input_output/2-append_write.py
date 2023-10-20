#!/usr/bin/python3
"""
Appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends text to filename.
    """

    with open(filename, 'a+') as f:
        return f.write(text)
