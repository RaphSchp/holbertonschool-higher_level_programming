#!/usr/bin/python3
"""
Module for readig a file
"""

def read_file(filename=""):
    """
    Read the contents of a text file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        file_contents = f.read()
        print(file_contents, end="")
