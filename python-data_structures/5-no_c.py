#!/usr/bin/python3
def no_c(my_string):
    x = ''
    for y in my_string:
        if y != 'c' and y != 'C':
            x += y
    return x
