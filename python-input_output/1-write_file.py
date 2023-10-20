#!/usr/bin/python3
"""
Module for writes a string to a text file
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file
    And returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        num_charcter_written = file.write(text)
        return num_charcter_written
