#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integer_count = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end='')
            integer_count += 1
        except (TypeError, ValueError):
            continue
    print('')
    return integer_count
