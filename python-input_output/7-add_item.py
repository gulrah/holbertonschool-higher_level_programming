#!/usr/bin/python3
"""Adds arguments to a Python list and saves them to a file."""

import sys
import os.path
from os import path
from json import dump, load
from sys import argv


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as f:
        dump(my_obj, f)


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    if not path.exists(filename):
        return []
    with open(filename, mode='r', encoding='utf-8') as f:
        return load(f)


args = sys.argv[1:]
filename = 'add_item.json'

if not path.exists(filename):
    save_to_json_file([], filename)

my_list = load_from_json_file(filename)
my_list.extend(args)
save_to_json_file(my_list, filename)
