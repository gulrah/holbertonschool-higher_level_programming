#!/usr/bin/python3
for x in range(99):
    if x < 98:
        print("{:02d}, ".format(x), end='')
    else:
        print("{:02d}".format(x))
