#!/usr/bin/python3
"""Function returns list of available attributes and methods of an object"""


def lookup(obj):
    """Return list of available attributes"""
    return (dir(obj))
