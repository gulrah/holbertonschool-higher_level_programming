#!/usr/bin/python3
import sys
from os import path
from json import dump, load
from typing import List


def save_to_json_file(my_obj: List, filename: str):
    """Save Python object to a file in JSON format."""
    with open(filename, mode='w', encoding='utf-8') as f:
        dump(my_obj, f)


def load_from_json_file(filename: str):
    """Load Python object from a file in JSON format."""
    if path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as f:
            return load(f)
    return []


def main():
    filename = 'add_item.json'
    args = sys.argv[1:]
    items_list = load_from_json_file(filename)
    items_list.extend(args)
    save_to_json_file(items_list, filename)


if __name__ == '__main__':
    main()
