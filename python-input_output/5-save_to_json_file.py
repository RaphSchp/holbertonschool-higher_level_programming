#!/usr/bin/python3
"""
Writes an Object to a text file,
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes the representation of my_obj
    to filename
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
