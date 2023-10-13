#!/usr/bin/python3
"""This is a module that contains a function

This function is going to be used to make the project of TDD
"""


def say_my_name(first_name, last_name=""):
    """Print a custom string

    Print a first name with its respective last name

    Args:
        first_name (str): The first name
        last_name (str): The last name

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
