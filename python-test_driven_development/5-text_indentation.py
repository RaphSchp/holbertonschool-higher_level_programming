#!/usr/bin/python3
"""This is a module that contains a function

This function is going to be used to make the project of TDD
"""


def text_indentation(text):
    """Print lines with 2 new lines

    Print a text with a specific condition:
        If a '.', '?' and ':' were found, add 2 new lines

    Args:
        text (str): The text to be used in this problem

    """
    if type(text) != str:
        raise TypeError("text must be a string")

    delimeter = ".?:"
    flag = 0
    new = str()

    for lett in text:
        if lett in delimeter:
            flag = 1
            new += lett
            new = new.strip()
            print(f"{new}", end="\n\n")
            new = str()
            continue
        flag = 0
        new += lett

    if not flag:
        new = new.strip()
        print(f"{new}", end="")
