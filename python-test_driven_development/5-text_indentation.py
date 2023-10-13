#!/usr/bin/python3
"""
Prints the text with new lines
"""


def text_indentation(text):
    """Prints the text with two new lines

    Parameters:
    Text: the text to be processed.

    Raises:
    TypeError: If text is not a string
    """

    # Validate text

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    SentenceSeparators = [".", "?", ":"]
    for char in text:
        print(char, end="")
        if char in SentenceSeparators:
            print("\n\n", end="")
