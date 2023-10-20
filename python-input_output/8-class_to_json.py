#!/usr/bin/python3
"""
Returns the dictionary description with
simple data structure
"""


def class_to_json(obj):
    """
    Creates a dict description of obj
    """

    return obj.__dict__
