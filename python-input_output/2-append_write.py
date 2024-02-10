#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8)
and returns the number of characters.
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file
    and returns the number of characters."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
