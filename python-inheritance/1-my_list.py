#!/usr/bin/python3
"""
Module for MyList class.
"""


class MyList(list):
    """
    Subclass of list.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))
