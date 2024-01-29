#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = sorted(a_dictionary.keys())
    for y in x:
        print("{}: {}".format(y, a_dictionary[y]))
