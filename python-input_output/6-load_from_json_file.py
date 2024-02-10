#!/usr/bin/python3
"""
Creates an Object from a JSON file.
"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file."""
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
