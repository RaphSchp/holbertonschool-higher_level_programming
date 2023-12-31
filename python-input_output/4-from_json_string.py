#!/usr/bin/python3
"""
Returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Return the object represented my my_str.
    """

    return json.loads(my_str)
