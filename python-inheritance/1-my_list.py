#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Function for sorting"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
