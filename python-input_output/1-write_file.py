#!/usr/bin/python3
"""
Writes a string to a text file (UTF8) and returns the number of characters.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
