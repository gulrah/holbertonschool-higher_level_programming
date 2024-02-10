#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then save them to a file.
"""

import sys
import os.path

if __name__ == "__main__":
    filename = "add_item.json"
    args = sys.argv[1:]
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            my_list = file.read()
            my_list = my_list.replace('\n', '').split(',')
            my_list = [item.strip(' "') for item in my_list if item.strip()]
    else:
        my_list = []
    
    my_list.extend(args)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(','.join(['"{}"'.format(item) for item in my_list]))
