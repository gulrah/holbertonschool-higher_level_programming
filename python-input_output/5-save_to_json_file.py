#!/usr/bin/python3
"""
Writes an Object to a text file, using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    import json
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)
