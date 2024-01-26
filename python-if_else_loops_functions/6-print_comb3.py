#!/usr/bin/python3
for x in range (10):
    for y in range(10):
        if x != y or y != x:
            print("{}{}".format(x, y), end=', ')
