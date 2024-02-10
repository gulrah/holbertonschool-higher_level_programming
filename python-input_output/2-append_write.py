#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file and returns the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
