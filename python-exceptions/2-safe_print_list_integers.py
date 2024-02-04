#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if not isinstance(my_list[i], int):
                raise ValueError("Value is not an integer")
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (IndexError, ValueError):
            pass
    print()
    return count
